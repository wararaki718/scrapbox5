use axum::response::Html;


pub async fn index() -> Html<&'static str> {
    Html("<h1>Hello, World!</h1>")
}
