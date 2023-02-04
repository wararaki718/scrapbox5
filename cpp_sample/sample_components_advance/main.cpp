#include <iostream>

#include "game_object.hpp"
#include "bjorn_graphics_component.hpp"
#include "bjorn_physics_component.hpp"
#include "graphics.hpp"
#include "player_input_component.hpp"
#include "world.hpp"

GameObject* createBjorn()
{
    return new GameObject(
        new PlayerInputComponent(),
        new BjornPhysicsComponent(),
        new BjornGraphicsComponent()
    );
}


int main()
{
    auto bjorn = createBjorn();
    auto graphics = Graphics();
    auto world = World();

    bjorn->update(world, graphics);
    std::cout << "DONE" << std::endl;

    return 0;
}