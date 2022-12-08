mod analyzer;
mod article;
mod loader;
mod parser;
mod train_test_split;

use linfa::Dataset;
use linfa::prelude::*;
use linfa_logistic::LogisticRegression;
use linfa_preprocessing::tf_idf_vectorization::TfIdfVectorizer;
use ndarray::Array;

use analyzer::TextAnalyzer;
use loader::ArticleLoader;
use train_test_split::train_test_split;


fn load(label: &str, analyzer: &TextAnalyzer, loader: &ArticleLoader) -> (Vec<String>, Vec<String>) {
    let mut texts = Vec::new();
    let articles = loader.load(label);
    for article in &articles {
        let text = analyzer.analyze(&article.content);
        texts.push(text.join(" "));
    }
    let labels = vec![label.to_string(); texts.len()];
    return (texts, labels);
}


fn main() {
    let text_analyzer = TextAnalyzer::new();
    let article_loader = ArticleLoader::new();

    let (it_texts, it_labels) = load("it-life-hack", &text_analyzer, &article_loader);
    let (sports_texts, sports_labels) = load("sports_watch", &text_analyzer, &article_loader);
    let texts = [it_texts, sports_texts].concat();
    let labels = [it_labels, sports_labels].concat();
    let (text_train, text_test, label_train, label_test) = train_test_split(texts, labels, Some(0.7 as f32), Some(true));

    let x_train = Array::from_vec(text_train);
    let x_test = Array::from_vec(text_test);
    let y_train = Array::from_vec(label_train);
    let y_test = Array::from_vec(label_test);

    //println!("{:?}", x);
    println!("{}, {:?}", x_train.ndim(), x_train.dim());
    println!("{:?}", y_train.shape());
    
    let vectorizer = TfIdfVectorizer::default().fit(&x_train).unwrap();
    //println!("{:?}", vectorizer.vocabulary());
    let train_features = vectorizer.transform(&x_train);
    let test_features = vectorizer.transform(&x_test);

    let train = Dataset::new(train_features.to_dense(), y_train);
    let test = Dataset::new(test_features.to_dense(), y_test);

    let model = LogisticRegression::default().max_iterations(150).fit(&train).unwrap();
    let preds = model.predict(&test);
    let cm = preds.confusion_matrix(&test).unwrap();

    println!("{:?}", cm);
    println!("accuracy: {}, MCC: {}", cm.accuracy(), cm.mcc());

    // println!("{:?}", vecs.shape());
    // println!("{:?}", y_test.shape());

    println!("DONE");
}
