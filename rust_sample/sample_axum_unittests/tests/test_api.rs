use axum::{
    body::{Body, BoxBody},
    http::{Request, Response, StatusCode, Method}
};
use tower::{Service, ServiceExt};
use std::convert::Infallible;

use sample_axum_unittests::app::get_app;


async fn call_service<S>(
    svc: &mut S,
    method: Method,
    uri: &str,
) -> (StatusCode, String)
where
    S: Service<Request<Body>, Response = Response<BoxBody>, Error = Infallible>
{
    let req = Request::builder().method(method).uri(uri).body(Body::empty()).unwrap();
    let res = svc.ready().await.unwrap().call(req).await.unwrap();

    let status = res.status();

    let body = res.into_body();
    let body = hyper::body::to_bytes(body).await.unwrap();
    let body = String::from_utf8(body.to_vec()).unwrap();

    (status, body)
}


#[tokio::test]
async fn test_ping() {
    let mut app = get_app();
    let (status, body) = call_service(&mut app, Method::GET, "/ping").await;

    assert_eq!(status, StatusCode::OK);
    assert_eq!(body, "pong");
}
