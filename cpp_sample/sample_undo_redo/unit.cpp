#include<iostream>
#include "unit.hpp"


void Unit::moveTo(int x_, int y_) {
    this->x_ = x_;
    this->y_ = y_;
}


int Unit::y() {
    return y_;
}


int Unit::x() {
    return x_;
}
