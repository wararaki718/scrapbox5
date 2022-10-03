use axum::{
    http::StatusCode,
    response::IntoResponse,
    Json
};

use crate::user::User;
use crate::message::Message;


pub async fn ping() -> &'static str {
    "pong"
}


pub async fn sample(Json(payload): Json<User>) -> impl IntoResponse {
    let message = Message {
        context: format!("hello {}", payload.name)
    };
    
    (StatusCode::OK, Json(message))
}
