use linfa::prelude::*;
use linfa_logistic::LogisticRegression;
use std::error::Error;


fn main() -> Result<(), Box<dyn Error>> {
    let (train, valid) = linfa_datasets::winequality().map_targets(|x| if *x > 6 {"good"} else {"bad"}).split_with_ratio(0.9);
    println!("the number of train: {}", train.nsamples());

    let model = LogisticRegression::default().max_iterations(150).fit(&train).unwrap();
    let pred = model.predict(&valid);

    let cm = pred.confusion_matrix(&valid).unwrap();
    println!("{:?}", cm);
    println!("accuracy: {}, MCC: {}", cm.accuracy(), cm.mcc());
    println!("DONE");

    Ok(())
}
