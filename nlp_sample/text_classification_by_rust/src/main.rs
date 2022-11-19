mod analyzer;
use analyzer::TextAnalyzer;
use linfa_preprocessing::tf_idf_vectorization::TfIdfVectorizer;
use ndarray::{ArrayBase, Ix1, Array};


fn main() {
    let text_analyzer = TextAnalyzer::new();
    let text = "東京でご飯を食べます。";
    let tokens = text_analyzer.analyze(text);
    for token in &tokens {
        println!("token: {}", token);
    }

    let x = ArrayBase::from_shape_vec((1, tokens.len()), tokens).unwrap();
    // let mut docs = vec![
    //     "東京でご飯を食べます。",
    //     "大阪でご飯を食べます。",
    //     "東京に行きます。",
    //     "京都に行きます。"
    // ];
    println!("{:?}", x);
    //let vectorizer = TfIdfVectorizer::default().fit(&x).unwrap();



    println!("DONE");
}
