use lindera::tokenizer::{Tokenizer, Token};


pub struct TextAnalyzer {
    tokenizer: Tokenizer
}


impl TextAnalyzer {
    pub fn new() -> Self {
        Self {
            tokenizer: Tokenizer::new().unwrap()
        }
    }
}


impl TextAnalyzer {
    pub fn analyze<'a>(&'a self, text: &'a str) -> Vec<&str> {
        let tokens = match self.tokenizer.tokenize(&text) {
            Ok(tokens) => tokens,
            Err(_e) => Vec::<Token>::new()
        };
        return tokens.into_iter().map(|token| { token.text }).collect();
    }
}
