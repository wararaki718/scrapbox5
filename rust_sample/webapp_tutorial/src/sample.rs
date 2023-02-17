use askama::Template;

#[derive(Template)]
#[template(path = "sample.html")]
pub struct Sample {
    pub message: String,
}
