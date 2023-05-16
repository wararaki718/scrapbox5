fn add(a: u32, b: u32) -> u32 {
    a + b
}

fn main() {
    let a: u32 = 1;
    let b: u32 = 2;
    let result: u32 = add(a, b);
    println!("{} + {} = {}", a, b, result);
    println!("DONE");
}
