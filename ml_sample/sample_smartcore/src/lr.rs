use smartcore::linalg::naive::dense_matrix::DenseMatrix;
use smartcore::linear::logistic_regression::LogisticRegression;
use smartcore::metrics::accuracy;


pub fn lr_classifier(x: &DenseMatrix<f32>, y: &Vec<f32>) -> f32 {
    let lr = LogisticRegression::fit(x, y, Default::default()).unwrap();
    let y_preds = lr.predict(x).unwrap();
    let result = accuracy(y, &y_preds);
    return result;
}