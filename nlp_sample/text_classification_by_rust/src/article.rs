#[derive(Debug)]
pub struct Article {
    pub url: Box<String>,
    pub datetime: Box<String>,
    pub title: Box<String>,
    pub content: Box<String>
}
