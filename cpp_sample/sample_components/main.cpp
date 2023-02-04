#include <iostream>
#include "bjorn.hpp"
#include "graphics.hpp"
#include "world.hpp"


int main()
{
    auto bjorn = Bjorn();
    auto graphics = Graphics();
    auto world = World();

    bjorn.update(world, graphics);
    std::cout << "DONE" << std::endl;

    return 0;
}