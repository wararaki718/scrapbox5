use smartcore::dataset::iris::load_dataset;
use smartcore::linalg::naive::dense_matrix::DenseMatrix;


pub fn load() -> (DenseMatrix<f32>, Vec<f32>){
    let iris = load_dataset();
    let x = DenseMatrix::from_array(
        iris.num_samples,
        iris.num_features,
        &iris.data
    );
    let y = iris.target;
    return (x, y);
}
