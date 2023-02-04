#ifndef PHYSICS_COMPONENT_HPP
#define PHYSICS_COMPONENT_HPP

#include "volume.hpp"
#include "world.hpp"

class Bjorn;

class PhysicsComponent
{
    public:
    PhysicsComponent()
    {
        volume_ = LARGE;
    }
    void update(Bjorn&, World&);

    private:
    Volume volume_;
};

#endif // PHYSICS_COMPONENT_HPP
