use ndarray::{Array1, Array};


fn main() {
    let mut x = Array1::<f64>::zeros(5);
    x += 0.5;
    println!("{:?}", x);


    let v = vec![1, 2, 3];
    let y = Array::from_shape_vec((1, 3), v).unwrap();
    println!("{:?}", y);

    println!("DONE");
}
