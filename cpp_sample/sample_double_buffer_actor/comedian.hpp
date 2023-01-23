#ifndef COMEDIAN_HPP
#define COMEDIAN_HPP

#include "actor.hpp"

class Comedian: public Actor
{
    public:
    void face(Actor* actor);
    virtual void update();

    private:
    Actor* facing_;
};

#endif // COMEDIAN_HPP
