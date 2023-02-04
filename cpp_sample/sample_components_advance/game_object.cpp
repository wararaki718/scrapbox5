#include "game_object.hpp"
#include "graphics.hpp"
#include "world.hpp"


void GameObject::update(World& world, Graphics& graphics)
{
    input_->update(*this);
    physics_->update(*this, world);
    graphics_->update(*this, graphics);
}
