use proconio::input;


fn main() {
    input! {
        n: i32,
        s: [String; n]
    }

    println!("{:?}", n);
    println!("{:?}", s);
    println!("DONE");
}
