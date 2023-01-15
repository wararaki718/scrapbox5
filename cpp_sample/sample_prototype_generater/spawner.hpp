#ifndef SPAWNER_HPP
#define SPAWNER_HPP

#include "monster.hpp"

Monster* spawnDemon();
Monster* spawnGhost();
Monster* spawnSorcerer();

typedef Monster* (*SpawnCallback)();

class Spawner
{
    public:
    Spawner(SpawnCallback spawn): spawn_(spawn) {}
    Monster* spawnMonster();

    private:
    SpawnCallback spawn_;
};

#endif // SPAWNER_HPP
