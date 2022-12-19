use std::io;
use std::time::Instant;

mod sort;
use sort::quick_sort;

mod sum;
use sum::{sum_of_squares, sum_of_squares_seq};


fn main() -> io::Result<()> {
    let begin = Instant::now();
    let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let result = sum_of_squares(&nums);
    println!("result={}, time={:?}", result, begin.elapsed());

    let begin = Instant::now();
    let nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let result2 = sum_of_squares_seq(&nums2);
    println!("result2={}, time={:?}", result2, begin.elapsed());
    
    let mut nums3 = vec![5, 6, 9, 10, 0, 1, 2, 7];
    quick_sort(&mut nums3);
    println!("{:?}", nums3);

    println!("DONE");
    Ok(())
}
