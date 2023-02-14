#include <iostream>
#include <cmath>

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
            handleCell(x, y);
        }
    }
}


void Grid::handleCell(int x, int y)
{
    auto unit = cells_[x][y];
    while (unit != nullptr)
    {
        handleUnit(unit, unit->next_);

        if(x > 0) handleUnit(unit, cells_[x-1][y]);
        if(y > 0) handleUnit(unit, cells_[x][y-1]);
        if(x > 0 && y > 0) handleUnit(unit, cells_[x-1][y-1]);
        if(x > 0 && y < NUM_CELLS - 1) handleUnit(unit, cells_[x-1][y+1]);

        unit = unit->next_;
    }
}


void Grid::handleUnit(Unit* unit, Unit* other)
{
    while(unit != nullptr)
    {
        while (other != nullptr)
        {
            if(distance(unit, other) < ATTACK_DISTANCE)
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


double Grid::distance(Unit* unit, Unit* other)
{
    double x = unit->x_ - other->x_;
    double y = unit->y_ - other->y_;
    return sqrt(pow(x, 2.0) + pow(y, 2.0));
}
