mod analyzer;
use analyzer::TextAnalyzer;


fn main() {
    let text_analyzer = TextAnalyzer::new();

    let text = "東京でご飯を食べます。";
    let tokens = text_analyzer.analyze(text);

    for token in tokens {
        println!("token: {}", token.text);
    }
    println!("DONE");
}
