#include <iostream>

#include "entity.hpp"


bool Entity::isHero()
{
    return hero;
}


bool Entity::isOnSurface()
{
    return surface;
}


void Entity::accelerate(Accelerate accelerate)
{
    accelerate_ = accelerate;
}


void Entity::update()
{
    std::cout << "entity status update" << std::endl;
}
