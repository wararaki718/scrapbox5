mod analyzer;
mod vectorizer;
use analyzer::TextAnalyzer;
use vectorizer::TfidfVectorizer;


fn main() {
    let text_analyzer = TextAnalyzer::new();
    let text = "東京でご飯を食べます。";
    let tokens = text_analyzer.analyze(text);
    for token in tokens {
        println!("token: {}", token.text);
    }

    let mut docs = vec![
        "東京でご飯を食べます。",
        "大阪でご飯を食べます。",
        "東京に行きます。",
        "京都に行きます。"
    ];

    let mut vectorizer = TfidfVectorizer::new();
    vectorizer.fit(&docs);
    println!("{:?}\n", vectorizer.feature_names());
    let vecs = vectorizer.transform(&docs);
    for vec in vecs {
        println!("{:?}", vec);
    }

    println!("DONE");
}
