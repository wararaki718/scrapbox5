#ifndef MONSTER_HPP
#define MONSTER_HPP

#include "breed.hpp"


class Monster
{
    public:
    Monster(Breed& breed): health_(breed.getHealth()), breed_(breed) {}
    const char* getAttack();

    private:
    int health_;
    Breed& breed_;
};

#endif // MONSTER_HPP
