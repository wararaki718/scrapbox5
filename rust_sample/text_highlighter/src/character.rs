use crate::link::LinkType;

#[derive(Debug, Eq)]
pub struct Character {
    pub index: u32,
    pub value: str,
    pub link: LinkType
}

impl Character {
    pub fn is_empty(&self) -> bool {
        self.value == ""
    }
}

impl Character {
    pub fn to_str(&self) -> &str {
        if self.value == "EOF" {
            return ""
        }
        &self.value
    }
}

impl PartialEq for Character {
    fn eq(&self, other: &Self) -> bool {
        self.value == other.value
    }
}
