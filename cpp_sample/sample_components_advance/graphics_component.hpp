#ifndef GRAPHICS_COMPONENT_HPP
#define GRAPHICS_COMPONENT_HPP

#include "graphics.hpp"

class GameObject;

class GraphicsComponent
{
    public:
    virtual ~GraphicsComponent() {}
    virtual void update(GameObject&, Graphics&) = 0;
};

#endif // GRAPHICS_COMPONENT_HPP
