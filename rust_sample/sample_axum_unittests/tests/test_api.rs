use axum::http::{StatusCode, Method};
use axum_test_helper::TestClient;

mod utils;
use utils::call_service;
use sample_axum_unittests::app::get_app;
use sample_axum_unittests::user::User;
use sample_axum_unittests::message::Message;


#[tokio::test]
async fn test_ping() {
    let mut app = get_app();
    let (status, body) = call_service(&mut app, Method::GET, "/ping").await;

    assert_eq!(status, StatusCode::OK);
    assert_eq!(body, "pong");
}


#[tokio::test]
async fn test_ping_pong() {
    let app = get_app();
    let client = TestClient::new(app);

    let response = client.get("/ping").send().await;
    assert_eq!(response.status(), StatusCode::OK);
    assert_eq!(response.text().await, "pong");
}


#[tokio::test]
async fn test_sample() {
    let app = get_app();
    let client = TestClient::new(app);

    let user = User { name: "sample_name".to_string() };
    let response = client.post("/sample").json(&user).send().await;

    assert_eq!(response.status(), StatusCode::OK);
    assert_eq!(response.json::<Message>().await.context, "hello sample_name");
}