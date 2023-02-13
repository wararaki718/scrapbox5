#include <iostream>

#include "particle.hpp"


void Particle::init(double x, double y, double xVel, double yVel, int lifetime)
{
    state_.live.x_ = x;
    state_.live.y_ = y;
    state_.live.xVel_ = xVel;
    state_.live.yVel_ = yVel;
    framesLeft_ = lifetime;
}


bool Particle::animate()
{
    if(!inUse()) {
        return false;
    }

    framesLeft_--;
    state_.live.x_ += state_.live.xVel_;
    state_.live.y_ += state_.live.yVel_;

    std::cout << "particle animate: (" << state_.live.x_ << ", " << state_.live.y_ << ", "<< framesLeft_ << ")" << std::endl;

    return framesLeft_ == 0;
}


bool Particle::inUse() const 
{
    return framesLeft_ > 0;
}


Particle* Particle::getNext() const
{
    return state_.next;
}


void Particle::setNext(Particle* next)
{
    state_.next = next;
}
