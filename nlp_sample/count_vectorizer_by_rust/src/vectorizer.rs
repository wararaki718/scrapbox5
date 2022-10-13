use std::collections::HashMap;


pub struct CountVectorizer {
    f_t: HashMap<String, i32>
}


impl CountVectorizer {
    pub fn new() -> Self {
        Self {
            f_t: HashMap::new()
        }
    }

    pub fn get_feature_names(self: &Self) -> Vec<String> {
        let mut names: Vec<String> = Vec::new();
        for key in self.f_t.keys() {
            names.push(key.to_string());
        }
        names
    }

    pub fn fit(&mut self, docs: Vec<Vec<&str>>) {
        for doc in docs {
            for term in doc {
                let key = term.to_string();
                if !self.f_t.contains_key(&key) {
                    self.f_t.insert(key, 1 as i32);
                } else {
                    if let Some(f) = self.f_t.get_mut(&key) {
                        *f += 1 as i32;
                    }
                }
            }
        }
    }

    pub fn transform(self: &Self, docs: Vec<Vec<&str>>) -> Vec<Vec<i32>> {
        let mut vectors: Vec<Vec<i32>> = Vec::new();
        for doc in docs {
            let mut vector: Vec<i32> = Vec::new();
            for (term, f) in &self.f_t {
                if let Some(_is_find) = (*doc).into_iter().find(|&x| x.to_string() == *term) {
                    vector.push(*f);
                } else {
                    vector.push(0 as i32);
                }
            }
            vectors.push(vector);
        }

        return vectors;
    }
}
