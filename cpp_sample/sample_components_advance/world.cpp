#include <iostream>

#include "volume.hpp"
#include "world.hpp"


void World::update()
{
    std::cout << "world update" << std::endl;
}


void World::resolveCollision(Volume volume, int x, int y, int velocity)
{
    std::cout << "collisiion" << std::endl;
}
