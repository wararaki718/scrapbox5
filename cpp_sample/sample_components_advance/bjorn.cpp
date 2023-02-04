#include "bjorn.hpp"
#include "graphics.hpp"
#include "world.hpp"


void Bjorn::update(World& world, Graphics& graphics)
{
    input_->update(*this);
    pyhsics_.update(*this, world);
    graphics_.update(*this, graphics);
}
