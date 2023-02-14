#include <iostream>

#include "grid.hpp"
#include "unit.hpp"


void Grid::add(Unit* unit)
{
    int cellX = (int)(unit->x_ / Grid::CELL_SIZE);
    int cellY = (int)(unit->y_ / Grid::CELL_SIZE);

    unit->prev_ = nullptr;
    unit->next_ = cells_[cellX][cellY];
    cells_[cellX][cellY] = unit;

    if (unit->next_ != nullptr)
    {
        unit->next_->prev_ = unit;
    }
}


void Grid::handleMelee()
{
    for (int x = 0; x < NUM_CELLS; x++)
    {
        for (int y = 0; y < NUM_CELLS; y++)
        {
            handleCell(cells_[x][y]);
        }
    }
}


void Grid::handleCell(Unit* unit)
{
    while(unit != nullptr)
    {
        auto other = unit->next_;
        while (other != nullptr)
        {
            if(unit->x_ == other->x_ && unit->y_ == other->y_)
            {
                handleAttack(unit, other);
            }
            other = other->next_;
        }
        unit = unit->next_;
    }
}


void Grid::handleAttack(Unit* unit, Unit* other)
{
    std::cout << "[attack] unit: (" << unit->x_ << ", " << unit->y_ << ")" << " -> other: (" << other->x_ << ", " << other->y_ << ")" << std::endl;
}


void Grid::move(Unit* unit, double x, double y)
{
    int oldCellX = (int)(unit->x_ / Grid::CELL_SIZE);
    int oldCellY = (int)(unit->y_ / Grid::CELL_SIZE);

    int cellX = (int)(x / Grid::CELL_SIZE);
    int cellY = (int)(y / Grid::CELL_SIZE);

    unit->x_ = x;
    unit->y_ = y;

    if(oldCellX == cellX && oldCellY == cellY)
    {
        return;
    }

    if(unit->prev_ != nullptr)
    {
        unit->prev_->next_ = unit->next_;
    }

    if(unit->next_ != nullptr)
    {
        unit->next_->prev_ = unit->prev_;
    }

    if(cells_[oldCellX][oldCellY] == unit)
    {
        cells_[oldCellX][oldCellY] = unit->next_;
    }

    add(unit);
}
