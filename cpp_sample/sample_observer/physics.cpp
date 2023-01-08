#include <iostream>

#include "accelerate.hpp"
#include "event.hpp"
#include "physics.hpp"


void Physics::updateEntity(Entity& entity)
{
    bool wasOnSurface = entity.isOnSurface();
    entity.accelerate(Accelerate::GRAVITY);
    entity.update();

    if (wasOnSurface && !entity.isOnSurface())
    {
        notify(entity, Event::EVENT_START_FALL);
    }
}


void Physics::notify(Entity& entity, Event event)
{
    std::cout << "notify event" << std::endl;
    std::cout << entity.isOnSurface() << std::endl;
    
    switch(event) {
        case Event::EVENT_START_FALL:
            std::cout << "fall" << std::endl;
            break;
    }
}
