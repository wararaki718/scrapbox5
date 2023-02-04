#ifndef BJORN_GRAPHICS_COMPONENT_HPP
#define BJORN_GRAPHICS_COMPONENT_HPP

#include "game_object.hpp"
#include "graphics.hpp"
#include "graphics_component.hpp"
#include "sprite.hpp"


class BjornGraphicsComponent: public GraphicsComponent
{
    public:
    BjornGraphicsComponent()
    {
        spriteStand_ = STAND;
        spriteWalkLeft_ = WALK_LEFT;
        spriteWalkRight_ = WALK_RIGHT;
    }

    void update(GameObject&, Graphics&);

    private:
    Sprite spriteStand_;
    Sprite spriteWalkLeft_;
    Sprite spriteWalkRight_;
};

#endif // BJORN_GRAPHICS_COMPONENT_HPP
