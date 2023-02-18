use axum::response::{Html, IntoResponse};
use crate::views::Sample;
use askama::Template;

pub async fn handler() -> Html<&'static str> {
    Html("<h1>Hello, World!</h1>")
}

pub async fn sample_handler() -> impl IntoResponse {
    let page = Sample {  message: "hello".to_string() };
    let html = page.render().unwrap();
    Html(html).into_response()
}

