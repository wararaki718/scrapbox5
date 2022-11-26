mod news;
mod parser;
use std::fs::File;
use std::io::{BufReader, Read};

use glob::glob;

use parser::parse;

fn main() {
    let mut filepaths = Vec::<String>::new();

    for entry in glob("./text/*/*.txt").expect("fail") {
        match entry {
            Ok(path) => {
                let filename = path.file_name().unwrap();
                if filename == "LICENSE.txt"{
                    continue;
                }
                //println!("{:?}", path.display());
                filepaths.push((*(path.to_str().unwrap())).to_string());
            },
            Err(e) => println!("{:?}", e)
        }
    }

    let file = File::open(&filepaths[0]).unwrap();
    let mut reader = BufReader::new(file);
    let mut content = String::new();
    reader.read_to_string(&mut content).unwrap();
    // println!("{}", content);

    let news = parse(&content);
    println!("{}", news.url);
    println!("{}", news.datetime);
    println!("{}", news.title);

    println!("DONE");
}
