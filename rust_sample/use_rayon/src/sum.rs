use rayon::prelude::*;


pub fn sum_of_squares(input: &[i32]) -> i32 {
    input.par_iter() // <-- just change that!
         .map(|&i| i * i)
         .sum()
}

pub fn sum_of_squares_seq(input: &[i32]) -> i32 {
    input.iter() // <-- just change that!
         .map(|&i| i * i)
         .sum()
}
