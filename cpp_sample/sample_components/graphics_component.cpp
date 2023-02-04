#include "bjorn.hpp"
#include "graphics.hpp"
#include "graphics_component.hpp"
#include "sprite.hpp"


void GraphicsComponent::update(Bjorn& bjorn, Graphics& graphics)
{
    Sprite* sprite = &spriteStand_;
    if (bjorn.velocity < 0) 
    {
        sprite = &spriteWalkLeft_;
    }
    else if (bjorn.velocity > 0)
    {
        sprite = &spriteWalkRight_;
    }

    graphics.draw(*sprite, bjorn.x, bjorn.y);
}
