use axum::{
    routing::{get, post},
    Router
};
use tower_http::trace::TraceLayer;

use crate::index::index;
use crate::api::{sample, ping};


pub fn get_app() -> Router {
    let app = Router::new()
        .route("/", get(index))
        .route("/ping", get(ping))
        .route("/sample", post(sample))
        .layer(TraceLayer::new_for_http());
    app
}
