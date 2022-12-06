use std::clone::Clone;
use rand::seq::SliceRandom;


pub fn train_test_split<T: Clone, S: Clone>(x: Vec<T>, y: Vec<S>, train_ratio: Option<f32>, random: Option<bool>) -> (Vec<T>, Vec<T>, Vec<S>, Vec<S>) {
    let mut x_new = x.clone();
    let mut y_new = y.clone();
    if random.unwrap_or(false) {
        let mut indices: Vec<usize> = Vec::<usize>::new();
        for i in 0..x.len() {
            indices.push(i);
        }
        indices.shuffle(&mut rand::thread_rng());
        let mut x_tmp = Vec::new();
        let mut y_tmp = Vec::new();
        for i in indices {
            x_tmp.push(x_new.get(i).unwrap());
            y_tmp.push(y_new.get(i).unwrap());
        }
        x_new = x_tmp.into_iter().cloned().collect();
        y_new = y_tmp.into_iter().cloned().collect();
    }

    let n_train = (train_ratio.unwrap_or(0.5) * x.len() as f32) as u32;
    let (x_train, x_test) = x_new.split_at(n_train.try_into().unwrap());
    let (y_train, y_test) = y_new.split_at(n_train.try_into().unwrap());

    return (x_train.to_vec(), x_test.to_vec(), y_train.to_vec(), y_test.to_vec());
}
