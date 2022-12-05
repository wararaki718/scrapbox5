use linfa::Dataset;
use ndarray::Array;
use ndarray::prelude::*;


fn main() {
    let x = Array::<f64, _>::zeros((10, 5));
    let y = Array::<f64, _>::zeros(10);
    
    let data = Dataset::new(x, y);

    println!("{:?}", data);

    let a = array![
        [1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8]
    ];
    let b = array![1, 2];

    let c = Dataset::new(a, b);
    println!("{:?}", c);
    println!("DONE");
}
