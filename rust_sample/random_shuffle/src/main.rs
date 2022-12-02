use rand::seq::SliceRandom;
use ndarray::{Array};


fn type_of<T>(_: &T) -> &'static str {
    std::any::type_name::<T>()
}


fn main() {
    let mut rng = rand::thread_rng();
    let s = String::from("abcdefghij");
    let mut items: Vec<u32> = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    println!("vector");
    println!("before: {:?}", items);
    items.shuffle(&mut rng);
    println!("after : {:?}", items);

    println!("array");
    let values = Array::from(items.clone());
    println!("before: {:?}", values);
    // values.shuffle(&mut rng);
    // println!("after : {:?}", values);
    let mut chars = Vec::<char>::new();
    for i in items {
        let tmp = s.chars().nth(i as usize - 1).unwrap();
        chars.push(tmp);
        // println!("{}, {}", tmp, type_of(&tmp));
    }
    let result: String = chars.iter().collect();
    println!("result: {}", result);
    println!("type  : {}", type_of(&result));

    println!("DONE");
}
