use smartcore::linalg::naive::dense_matrix::DenseMatrix;
use smartcore::neighbors::knn_classifier::KNNClassifier;
use smartcore::metrics::accuracy;


pub fn knn_classifier(x: &DenseMatrix<f32>, y: &Vec<f32>) -> f32{
    let knn = KNNClassifier::fit(
        x,
        y,
        Default::default()
    ).unwrap();

    let y_preds = knn.predict(x).unwrap();
    let result = accuracy(y, &y_preds);
    return result;
}
