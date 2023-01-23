#ifndef STAGE_HPP
#define STAGE_HPP

#include "actor.hpp"

class Stage
{
    public:
    void add(Actor*, int);
    void update();

    private:
    static const int NUM_ACTORS = 3;
    Actor* actors_[NUM_ACTORS];
};

#endif // STAGE_HPP
