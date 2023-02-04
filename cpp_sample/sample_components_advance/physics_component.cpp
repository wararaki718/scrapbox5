#include "bjorn.hpp"
#include "physics_component.hpp"
#include "world.hpp"


void PhysicsComponent::update(Bjorn& bjorn, World& world)
{
    bjorn.x += bjorn.velocity;
    world.resolveCollision(volume_, bjorn.x, bjorn.y, bjorn.velocity);
}
