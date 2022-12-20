use unicode_normalization::UnicodeNormalization;
use unicode_segmentation::UnicodeSegmentation;

fn main() {
    // use unicode_normalization
    let s = "ｈello";
    let c = s.nfkc().collect::<String>();
    println!("{} -> {}", s, c);

    // use unicode_segmentation
    let t = "ｈello";
    let d = t.graphemes(true).collect::<String>();
    println!("{} -> {}", t, d);
    println!("DONE");
}
