use std::mem;

mod point;
mod rectangle;
use rectangle::Rectangle;
use point::Point;


fn origin() -> Point {
    Point {
        x: 0.0,
        y: 0.0
    }
}


fn boxed_origin() -> Box<Point> {
    Box::new(Point { x: 0.0, y: 0.0 })
}


fn main() {
    // stack
    let point: Point = origin();
    let rectangle: Rectangle = Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 }
    };

    // heap
    let boxed_rectangle: Box<Rectangle> = Box::new(
        Rectangle {
            top_left: origin(),
            bottom_right: Point { x: 3.0, y: -4.0 }
        }
    );
    let boxed_point: Box<Point> = Box::new(origin());

    let box_in_a_box: Box<Box<Point>> = Box::new(boxed_origin());

    // stack
    println!("Point occupies {} bytes on the stack", mem::size_of_val(&point));
    println!("Rectangle occupies {} bytes on the stack", mem::size_of_val(&rectangle));

    // heap
    println!("Boxed point occupies {} bytes on the heap", mem::size_of_val(&boxed_point));
    println!("Boxed rectangle occupies {} bytes on the heap", mem::size_of_val(&boxed_rectangle));
    println!("Boxed box occupies {} bytes on the heap", mem::size_of_val(&box_in_a_box));

    // heap -> stack?
    let unboxed_point: Point = *boxed_point;
    println!("Unboxed point occupies {} bytes on the stack", mem::size_of_val(&unboxed_point));

    println!("DONE");
}
