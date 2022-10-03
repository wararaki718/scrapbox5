use std::net::SocketAddr;

mod api;
mod app;
mod index;
mod message;
mod user;
use app::get_app;


#[tokio::main]
async fn main() {
    let app = get_app();

    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    println!("listening on {}", addr);
    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();

    println!("DONE");
}
