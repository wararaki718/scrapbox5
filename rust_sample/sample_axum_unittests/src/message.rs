use serde::{Deserialize, Serialize};


#[derive(Deserialize, Serialize)]
pub struct Message {
    pub context: String
}
