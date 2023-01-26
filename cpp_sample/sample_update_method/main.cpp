#include <iostream>

#include "skeleton.hpp"
#include "statue.hpp"
#include "world.hpp"


int main()
{
    auto world = World();
    auto skeleton = new Skeleton();
    auto statue = new Statue(1);

    world.add(skeleton);
    world.add(statue);

    world.gameLoop();

    std::cout << "DONE" << std::endl;
    return 0;
}
