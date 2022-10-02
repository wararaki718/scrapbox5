use sample_unittests::sample::{addf, addu};


fn main() {
    let x: u32 = 1;
    let y: u32 = 2;

    let a: f32 = 1.5;
    let b: f32 = 2.0;

    let result1 = addu(x, y);
    let result2 = addf(a, b);

    println!("addu({}, {})={}", x, y, result1);
    println!("addf({}, {})={}", a, b, result2);

    println!("DONE");
}
