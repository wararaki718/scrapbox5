mod train_test_split;
use crate::train_test_split::train_test_split;

fn main() {
    let x = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];
    let y = vec!["a", "b", "c", "d", "e", "f", "g", "h", "i"];
    let (x_train, x_test, y_train, y_test) = train_test_split(x, y, Some(0.8 as f32), Some(true));
    println!("x_train={:?}", x_train);
    println!("x_test ={:?}", x_test);
    println!("y_train={:?}", y_train);
    println!("y_test ={:?}", y_test);
    println!("DONE");
}
