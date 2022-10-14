use std::collections::HashMap;

use crate::analyzer::TextAnalyzer;


pub struct CountVectorizer {
    f_t: HashMap<String, i32>,
    analyzer: TextAnalyzer
}


impl CountVectorizer {
    pub fn new() -> Self {
        Self {
            f_t: HashMap::new(),
            analyzer: TextAnalyzer::new()
        }
    }

    pub fn get_feature_names(self: &Self) -> Vec<String> {
        let mut names: Vec<String> = Vec::new();
        for key in self.f_t.keys() {
            names.push(key.to_string());
        }
        names
    }

    fn analyze(&mut self, doc: &str) -> Vec<String> {
        let mut terms: Vec<String> = Vec::new();
        for token in self.analyzer.analyze(doc) {
            terms.push(token.text.to_string());
        }
        terms
    }

    pub fn fit(&mut self, docs: Vec<&str>) {
        for doc in docs {
            for term in self.analyze(doc) {
                if !self.f_t.contains_key(&term) {
                    self.f_t.insert(term, 1 as i32);
                } else {
                    if let Some(f) = self.f_t.get_mut(&term) {
                        *f += 1 as i32;
                    }
                }
            }
        }
    }

    pub fn transform(self: &mut Self, docs: Vec<&str>) -> Vec<Vec<i32>> {
        let mut vectors: Vec<Vec<i32>> = Vec::new();
        for doc in docs {
            let mut vector: Vec<i32> = Vec::new();
            let words = self.analyze(doc);
            for (term, f) in &self.f_t {
                if let Some(_is_find) = words.clone().into_iter().find(|x| *x == *term) {
                    vector.push(*f);
                } else {
                    vector.push(0 as i32);
                }
            }
            vectors.push(vector);
        }

        vectors
    }
}
