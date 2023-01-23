#include "comedian.hpp"


void Comedian::face(Actor* actor)
{
    facing_ = actor;
}


void Comedian::update()
{
    if(wasSlapped()){
        facing_->slap();
    }
}
