#ifndef SPAWNER_HPP
#define SPAWNER_HPP

#include "monster.hpp"


class Spawner
{
    public:
    Spawner(Monster* prototype): prototype_(prototype) {}
    Monster* spawnMonster();

    private:
    Monster* prototype_;
};

#endif // SPAWNER_HPP
