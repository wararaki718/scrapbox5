#include <iostream>
#include "move.hpp"


void MoveUnitCommand::execute() {
    xBefore_ = unit_->x();
    yBefore_ = unit_->y();
    unit_->moveTo(x_, y_);
    std::cout << "move x: " << x_ << ",y: " << y_ << std::endl;
}

void MoveUnitCommand::undo() {
    unit_->moveTo(xBefore_, yBefore_);
    std::cout << "undo" << std::endl;
}