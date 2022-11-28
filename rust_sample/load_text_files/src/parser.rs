use crate::news::News;


pub fn parse(text: &str) -> News {
    let mut lines: Vec<&str> = text.rsplit("\n").collect();

    let url = lines.pop();
    let datetime = lines.pop();
    let title = lines.pop();

    lines.reverse();
    let content = lines.join("\n");
    
    return News {
        url: Box::<String>::new((*url.unwrap()).to_string()),
        datetime: Box::<String>::new((*datetime.unwrap()).to_string()),
        title: Box::<String>::new((*title.unwrap()).to_string()),
        content: Box::<String>::new((*content).to_string())
    };
}