#ifndef BJORN_PHYSICS_COMPONENT_HPP
#define BJORN_PHYSICS_COMPONENT_HPP

#include "game_object.hpp"
#include "physics_component.hpp"
#include "volume.hpp"
#include "world.hpp"

class BjornPhysicsComponent: public PhysicsComponent
{
    public:
    BjornPhysicsComponent()
    {
        volume_ = LARGE;
    }
    void update(GameObject&, World&);

    private:
    Volume volume_;
};

#endif // BJORN_PHYSICS_COMPONENT_HPP
