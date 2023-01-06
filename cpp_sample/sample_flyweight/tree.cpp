#include <iostream>

#include "tree.hpp"


void Tree::show(void) {
    std::cout << &model_ << std::endl;
    std::cout << position_.x << ", " << position_.y << ", " << position_.z << std::endl;
}
