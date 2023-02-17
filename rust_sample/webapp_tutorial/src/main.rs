mod sample;

use axum::{response::{Html, IntoResponse}, routing::get, Router};
use std::net::SocketAddr;
use askama::Template;

use sample::Sample;

#[tokio::main]
async fn main() {
    if std::env::var_os("RUST_LOG").is_none() {
        std::env::set_var("RUST_LOG", "webapp=debug");
    }
    tracing_subscriber::fmt::init();

    let app = Router::new()
        .route("/", get(handler))
        .route("/sample", get(sample_handler));

    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    tracing::debug!("listening on {}", addr);
    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}

async fn handler() -> Html<&'static str> {
    Html("<h1>Hello, World!</h1>")
}

async fn sample_handler() -> impl IntoResponse {
    let page = Sample {  message: "hello".to_string() };
    let html = page.render().unwrap();
    Html(html).into_response()
}
