#include "grid.hpp"
#include "unit.hpp"


Unit::Unit(Grid* grid, double x, double y): x_(x), y_(y), grid_(grid) {
    grid_->add(this);
}


void Unit::move(double x, double y)
{
    grid_->move(this, x, y);
}