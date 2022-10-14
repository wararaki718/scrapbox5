mod vectorizer;
mod analyzer;
use vectorizer::CountVectorizer;


fn main() {
    let data = vec![
        "hello world",
        "hello ping",
        "apple pen",
        "pen world",
        "東京でご飯を食べます。",
        "大阪でご飯を食べます。",
        "東京に行きます。",
        "京都に行きます。"
    ];
    println!("{:?}", data);
    let mut vectorizer = CountVectorizer::new();
    vectorizer.fit(data.clone());

    let names = vectorizer.get_feature_names();
    println!("{:?}", names);

    let vectors = vectorizer.transform(data.clone());
    for vector in vectors {
        println!("{:?}", vector);
    }

    println!("DONE");
}
