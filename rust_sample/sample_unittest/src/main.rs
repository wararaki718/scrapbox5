mod calc;
use calc::*;


fn main() {
    let a = add(1, 2);
    let b = minus(2, 1);
    let c = multiply(1, 2);
    let d = divide(4, 2);
    println!("{}, {}, {}, {}", a, b, c, d);
    println!("DONE");
}
