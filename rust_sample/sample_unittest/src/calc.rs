pub fn add(a: u32, b: u32) -> u32 {
    a + b
}

pub fn minus(a: u32, b: u32) -> u32 {
    a - b
}

pub fn multiply(a: u32, b: u32) -> u32 {
    a * b
}

pub fn divide(a: u32, b: u32) -> f32 {
    if b == 0 {
        panic!("divide zero");
    }
    (a / b) as f32
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

    #[test]
    fn test_minus() {
        assert_eq!(minus(2, 1), 1);
    }

    #[test]
    fn test_multiply() {
        assert_eq!(multiply(1, 2), 2);
    }

    #[test]
    fn test_divide() {
        assert_eq!(divide(4, 2), 2.0);
    }

    #[test]
    #[should_panic]
    fn test_divide_panic(){
        divide(1, 0);
    }
}