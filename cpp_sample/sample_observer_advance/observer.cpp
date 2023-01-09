#include <iostream>

#include "entity.hpp"
#include "event.hpp"
#include "observer.hpp"


void Observer::onNotify(Entity& entity, Event event)
{
    std::cout << "observer on notify." << std::endl;
}
