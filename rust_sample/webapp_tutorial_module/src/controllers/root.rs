use axum::Router;
use axum::routing::get;

use crate::response::{handler, sample_handler};

pub fn app() -> Router {
    let app = Router::new()
        .route("/", get(handler))
        .route("/sample", get(sample_handler));
    app
}
