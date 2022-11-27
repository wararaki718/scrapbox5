mod analyzer;
mod article;
mod loader;
mod parser;

use linfa_preprocessing::tf_idf_vectorization::TfIdfVectorizer;
use ndarray::Array;

use analyzer::TextAnalyzer;
use loader::ArticleLoader;


fn main() {
    let text_analyzer = TextAnalyzer::new();
    let article_loader = ArticleLoader::new();

    let articles = article_loader.load("it-life-hack");
    let mut texts = Vec::new();
    for article in &articles {
        let text = text_analyzer.analyze(&article.content);
        texts.push(text.join(" "));
    }
    let x = Array::from_vec(texts);
    //println!("{:?}", x);
    println!("{}, {:?}", x.ndim(), x.dim());
    
    let vectorizer = TfIdfVectorizer::default().fit(&x).unwrap();
    //println!("{:?}", vectorizer.vocabulary());
    
    let vecs = vectorizer.transform(&x);
    println!("{:?}", vecs.shape());

    println!("DONE");
}
