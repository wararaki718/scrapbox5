#ifndef AI_COMPONENT_HPP
#define AI_COMPONENT_HPP

#include "animation.hpp"
#include "lootdrop.hpp"
#include "vector.hpp"


class AIComponent
{
    public:
    void update();

    private:
    Animation* animation_;
    double energy_;
    Vector goalPos_;

    LootDrop* loot_;
};

#endif // AI_COMPONENT_HPP