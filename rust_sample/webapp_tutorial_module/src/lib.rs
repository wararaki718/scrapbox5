mod response;

mod controllers {
    mod root;
    pub use root::app;
}

pub use controllers::app;

mod views {
    mod sample;
    pub use sample::Sample;
}
