fn curring(x: u32, y: u32) -> (u32, u32) {
    let add = |x| move |y| x + y; // curring
    let result = add(x)(y);
    let increment = add(x);
    let result2 = increment(y);
    return (result, result2);
}

fn partial_function(x: u32, y: u32) -> (u32, u32) {
    let add = |x, y| x + y; // partial
    let result = add(x, y);
    let increment = add(x, y);
    let result2 = increment; // ?
    return (result, result2);
}

fn main() {
    let x: u32 = 1;
    let y: u32 = 2;
    let (c1, c2) = curring(x, y);
    let (p1, p2) = partial_function(x, y);
    
    println!("c1={}, c2={}", c1, c2);
    println!("p1={}, p2={}", p1, p2);
    println!("DONE");
}
