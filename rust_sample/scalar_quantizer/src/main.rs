mod quantizer;
use quantizer::encode_fp16;

fn main() {
    let val: f32 = 1.0;
    let result = encode_fp16(val);
    println!("result: {}", result);
    println!("DONE");
}
