use sample_unittests::sample::{addf, addu};


#[test]
fn add_float() {
    let x: f32 = 1.5;
    let y: f32 = 2.0;

    let result = addf(x, y);
    let expected: f32 = 3.5;
    assert_eq!(result.to_bits(), expected.to_bits());
}

#[test]
fn add_uint() {
    let x: u32 = 1;
    let y: u32 = 2;
    let result = addu(x, y);
    let expected: u32 = 3;
    assert_eq!(result, expected);
}