#include "actor.hpp"


void Actor::swap()
{
    currentSlapped_ = nextSlapped_;
    nextSlapped_ = false;
}


void Actor::slap()
{
    nextSlapped_ = true;
}


bool Actor::wasSlapped()
{
    return currentSlapped_;
}
