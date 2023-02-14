#include <iostream>

#include "grid.hpp"
#include "unit.hpp"


int main()
{
    auto grid = new Grid();
    std::cout << "add" << std::endl;
    auto unit1 = new Unit(grid, 20., 0.);
    auto unit2 = new Unit(grid, 80., 0.);
    grid->handleMelee();

    std::cout << "move" << std::endl;
    unit1->move(40., 0.);
    unit2->move(40., 0.);
    grid->handleMelee();

    std::cout << "DONE" << std::endl;
    return 0;
}
