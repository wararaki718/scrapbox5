use rand::seq::SliceRandom;


fn main() {
    let mut rng = rand::thread_rng();
    let mut items: Vec<u32> = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    println!("before: {:?}", items);
    items.shuffle(&mut rng);
    println!("after : {:?}", items);

    println!("DONE");
}
