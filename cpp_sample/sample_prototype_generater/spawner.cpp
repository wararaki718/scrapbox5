#include "demon.hpp"
#include "ghost.hpp"
#include "sorcerer.hpp"
#include "spawner.hpp"


Monster* spawnDemon()
{
    return new Demon();
}


Monster* spawnGhost()
{
    return new Ghost();
}


Monster* spawnSorcerer()
{
    return new Sorcerer();
}


Monster* Spawner::spawnMonster()
{
    return spawn_();
}
