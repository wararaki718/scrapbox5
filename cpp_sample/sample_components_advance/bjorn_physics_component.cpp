#include "bjorn_physics_component.hpp"
#include "game_object.hpp"
#include "world.hpp"


void BjornPhysicsComponent::update(GameObject& obj, World& world)
{
    obj.x += obj.velocity;
    world.resolveCollision(volume_, obj.x, obj.y, obj.velocity);
}
