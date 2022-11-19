mod analyzer;
use analyzer::TextAnalyzer;
use linfa_preprocessing::tf_idf_vectorization::TfIdfVectorizer;
use ndarray::{Array1, Ix1};


fn main() {
    let text_analyzer = TextAnalyzer::new();
    let text = "東京でご飯を食べます。";
    let tokens = text_analyzer.analyze(text);
    for token in tokens {
        println!("token: {}", token);
    }

    // let mut docs = vec![
    //     "東京でご飯を食べます。",
    //     "大阪でご飯を食べます。",
    //     "東京に行きます。",
    //     "京都に行きます。"
    // ];
    //let vectorizer = TfIdfVectorizer::default().fit(tokens).unwrap();



    println!("DONE");
}
