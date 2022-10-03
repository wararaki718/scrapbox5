use axum::http::{StatusCode, Method};

mod utils;
use utils::call_service;
use sample_axum_unittests::app::get_app;


#[tokio::test]
async fn test_ping() {
    let mut app = get_app();
    let (status, body) = call_service(&mut app, Method::GET, "/ping").await;

    assert_eq!(status, StatusCode::OK);
    assert_eq!(body, "pong");
}
