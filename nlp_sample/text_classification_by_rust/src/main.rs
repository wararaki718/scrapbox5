mod analyzer;
use analyzer::TextAnalyzer;
use linfa_preprocessing::tf_idf_vectorization::TfIdfVectorizer;
use ndarray::Array;


fn main() {
    let text_analyzer = TextAnalyzer::new();

    let docs = vec![
        "東京でご飯を食べます。",
        "大阪でご飯を食べます。",
        "東京に行きます。",
        "京都に行きます。"
    ];
    let mut texts = Vec::new();
    for doc in &docs {
        let text = text_analyzer.analyze(doc);
        texts.push(text.join(" "));
    }
    let x = Array::from_vec(texts);
    println!("{:?}", x);
    println!("{}, {:?}", x.ndim(), x.dim());
    
    let vectorizer = TfIdfVectorizer::default().fit(&x).unwrap();
    println!("{:?}", vectorizer.vocabulary());
    
    let vecs = vectorizer.transform(&x);
    println!("{:?}", vecs);

    println!("DONE");
}
