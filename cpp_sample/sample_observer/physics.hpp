#ifndef PHYSICS_HPP
#define PHYSICS_HPP

#include "entity.hpp"
#include "event.hpp"


class Physics
{
    public:
    void updateEntity(Entity& entity);
    
    private:
    void notify(Entity&, Event);
};


#endif // PHYSICS_HPP
