mod analyzer;
use analyzer::TextAnalyzer;
use linfa_preprocessing::tf_idf_vectorization::TfIdfVectorizer;
use ndarray::Array;


fn main() {
    let text_analyzer = TextAnalyzer::new();
    let text = "東京でご飯を食べます。";
    let tokens = text_analyzer.analyze(text);
    for token in &tokens {
        println!("token: {}", token);
    }

    let docs = vec![
        "東京 で ご飯 を 食べ ます 。",
        "大阪 で ご飯 を 食べ ます 。",
        "東京 に 行き ます 。",
        "京都 に 行き ます 。"
    ];
    // let docs = vec![
    //     "I have a pen",
    //     "This is a pen",
    //     "you have a pen",
    //     "that is an apple"
    // ];
    let x = Array::from_vec(docs);
    println!("{:?}", x);
    println!("{}, {:?}", x.ndim(), x.dim());
    
    let vectorizer = TfIdfVectorizer::default().fit(&x).unwrap();
    println!("{:?}", vectorizer.vocabulary());


    println!("DONE");
}
