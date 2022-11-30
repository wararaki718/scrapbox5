use std::{io, thread};
use std::time::Duration;


fn main() -> io::Result<()> {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("launch thread: {}", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    // wait thread
    //handle.join().unwrap();

    for i in 1..5 {
        println!("sleep main: {}", i);
        thread::sleep(Duration::from_millis(1));
    }

    // wait thread
    handle.join().unwrap();

    println!("DONE");

    Ok(())
}
