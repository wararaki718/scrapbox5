#include <iostream>

#include "bjorn.hpp"
#include "graphics.hpp"
#include "player_input_component.hpp"
#include "world.hpp"


int main()
{
    auto bjorn = Bjorn(new PlayerInputComponent());
    auto graphics = Graphics();
    auto world = World();

    bjorn.update(world, graphics);
    std::cout << "DONE" << std::endl;

    return 0;
}