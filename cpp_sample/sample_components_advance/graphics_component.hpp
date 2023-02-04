#ifndef GRAPHICS_COMPONENT_HPP
#define GRAPHICS_COMPONENT_HPP

#include "graphics.hpp"
#include "sprite.hpp"

class Bjorn;

class GraphicsComponent
{
    public:
    GraphicsComponent()
    {
        spriteStand_ = STAND;
        spriteWalkLeft_ = WALK_LEFT;
        spriteWalkRight_ = WALK_RIGHT;
    }

    void update(Bjorn&, Graphics&);

    private:
    Sprite spriteStand_;
    Sprite spriteWalkLeft_;
    Sprite spriteWalkRight_;
};

#endif // GRAPHICS_COMPONENT_HPP
