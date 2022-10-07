use axum::http::{StatusCode};
use axum_test_helper::TestClient;

use sample_axum_unittests::app::get_app;


#[tokio::test]
async fn test_index() {
    let app = get_app();

    let client = TestClient::new(app);
    let response = client.get("/").send().await;
    assert_eq!(response.status(), StatusCode::OK);
    assert_eq!(response.text().await, "<h1>Hello, World!</h1>");
}
