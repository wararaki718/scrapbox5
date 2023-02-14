#ifndef UNIT_HPP
#define UNIT_HPP

class Grid;

class Unit
{
    friend class Grid;

    public:
    Unit(Grid* grid, double x, double y);
    void move(double x, double y);

    double x_;
    double y_;
    Grid* grid_;
    private:
    Unit* prev_;
    Unit* next_;
};

#endif // UNIT_HPP
