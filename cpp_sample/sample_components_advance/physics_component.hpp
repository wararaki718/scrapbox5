#ifndef PHYSICS_COMPONENT_HPP
#define PHYSICS_COMPONENT_HPP

#include "world.hpp"

class GameObject;

class PhysicsComponent
{
    public:
    virtual ~PhysicsComponent() {}
    virtual void update(GameObject&, World&) = 0;
};


#endif // PHYSICS_COMPONENT_HPP
