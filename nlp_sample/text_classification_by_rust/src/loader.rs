use std::fs::File;
use std::io::{BufReader, Read};

use glob::glob;

use crate::article::Article;
use crate::parser::ArticleParser;


pub struct ArticleLoader {
    parser: ArticleParser
}


impl ArticleLoader {
    pub fn new() -> Self {
        Self {
            parser: ArticleParser::new()
        }
    }
}


impl ArticleLoader {
    fn _load(&self, filepath: &str) -> String {
        let file = File::open(filepath).unwrap();
        let mut reader = BufReader::new(file);
        let mut content = String::new();
        reader.read_to_string(&mut content).unwrap();
        return content;
    }

    pub fn load(&self, topic: &str) -> Vec<Article> {
        let mut articles = Vec::<Article>::new();
        let dir_path = (vec!["./text/", topic, "/*.txt"]).concat();

        for entry in glob(&dir_path).expect("fail") {
            match entry {
                Ok(path) => {
                    let filename = path.file_name().unwrap();
                    if filename == "LICENSE.txt"{
                        continue;
                    }
                    let content = self._load(&path.to_str().unwrap());
                    let article = self.parser.parse(&content);
                    articles.push(article);
                },
                Err(e) => println!("{:?}", e)
            }
        }

        return articles;
    }
}
