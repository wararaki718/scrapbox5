#ifndef SPAWNER_HPP
#define SPAWNER_HPP

#include "monster.hpp"


class Spawner
{
    public:
    virtual ~Spawner() {}
    virtual Monster* spawnMonster() = 0;
};

template <class T>
class SpawnerFor: public Spawner
{
    public:
    virtual Monster* spawnMonster() { return new T(); };
};

#endif // SPAWNER_HPP
