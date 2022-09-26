mod dataset;
mod knn;
mod lr;

use dataset::load;
use knn::knn_classifier;
use lr::lr_classifier;


fn main() {
    let (x, y) = load();
    let knn_result = knn_classifier(&x, &y);
    let lr_result = lr_classifier(&x, &y);

    println!("knn: {}", knn_result);
    println!("lr : {}", lr_result);
    println!("DONE");
}
