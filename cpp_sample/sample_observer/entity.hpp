#ifndef ENTITY_HPP
#define ENTITY_HPP

#include "accelerate.hpp"


class Entity
{
    public:
    Entity() {}
    Entity(bool hero_): hero(hero_) {}

    bool isHero();
    bool isOnSurface();
    void accelerate(Accelerate);
    void update();

    private:
    bool surface{true};
    Accelerate accelerate_{Accelerate::NONE};
    bool hero{false};
};

#endif // ENTITY_HPP
