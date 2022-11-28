#[derive(Debug)]
pub struct News {
    pub url: Box<String>,
    pub datetime: Box<String>,
    pub title: Box<String>,
    pub content: Box<String>
}
