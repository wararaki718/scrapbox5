#include <iostream>

#include "particle.hpp"


void Particle::init(double x, double y, double xVel, double yVel, int lifetime)
{
    x_ = x;
    y_ = y;
    xVel_ = xVel;
    yVel_ = yVel;
    framesLeft_ = lifetime;
}


void Particle::animate()
{
    if(!inUse()) {
        return;
    }

    framesLeft_--;
    x_ += xVel_;
    y_ += yVel_;

    std::cout << "particle animate: (" << x_ << ", " << y_ << ", "<< framesLeft_ << ")" << std::endl;
}


bool Particle::inUse() const 
{
    return framesLeft_ > 0;
}
