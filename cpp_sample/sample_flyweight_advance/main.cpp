#include <iostream>

#include "position.hpp"
#include "world.hpp"


int main()
{
    World world = World();
    world.generateTerrain();

    int cost = world.getTile(2, 3).getMoveCost();
    std::cout << cost << std::endl;

    std::cout << "DONE" << std::endl;
    return 0;
}
