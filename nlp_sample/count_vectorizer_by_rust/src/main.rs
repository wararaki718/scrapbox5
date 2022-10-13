mod vectorizer;
use vectorizer::CountVectorizer;

fn main() {
    let data = vec![
        vec!["hello", "world"],
        vec!["hello", "ping"],
        vec!["apple", "pen"],
        vec!["pen", "world"]
    ];
    println!("{:?}", data);
    let mut vectorizer = CountVectorizer::new();
    vectorizer.fit(data.clone());

    let names = vectorizer.get_feature_names();
    println!("{:?}", names);

    let vectors = vectorizer.transform(data.clone());
    println!("{:?}", vectors);

    println!("DONE");
}
