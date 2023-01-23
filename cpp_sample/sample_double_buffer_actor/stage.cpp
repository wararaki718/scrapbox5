#include "actor.hpp"
#include "stage.hpp"


void Stage::add(Actor* actor, int index)
{
    actors_[index] = actor;
}


void Stage::update()
{
    for (int i = 0; i < NUM_ACTORS; i++) {
        actors_[i]->update();
    }
    for (int i = 0; i < NUM_ACTORS; i++) {
        actors_[i]->swap();
    }
}
