#include "game_object.hpp"
#include "graphics.hpp"
#include "bjorn_graphics_component.hpp"
#include "sprite.hpp"


void BjornGraphicsComponent::update(GameObject& obj, Graphics& graphics)
{
    Sprite* sprite = &spriteStand_;
    if (obj.velocity < 0) 
    {
        sprite = &spriteWalkLeft_;
    }
    else if (obj.velocity > 0)
    {
        sprite = &spriteWalkRight_;
    }

    graphics.draw(*sprite, obj.x, obj.y);
}
