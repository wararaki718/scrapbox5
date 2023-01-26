#include "entity.hpp"


double Entity::x() const
{
    return x_;
}


double Entity::y() const
{
    return y_;
}


void Entity::setX(double x)
{
    x_ = x;
}


void Entity::setY(double y)
{
    y_ = y;
}
