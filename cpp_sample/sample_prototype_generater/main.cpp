#include <iostream>

#include "spawner.hpp"


int main()
{
    Spawner* ghostSpawner = new Spawner(spawnGhost);
    Spawner* demonSpawner = new Spawner(spawnDemon);
    Spawner* sorcererSpawner = new Spawner(spawnSorcerer);

    auto ghost = ghostSpawner->spawnMonster();
    ghost->show();

    auto demon = demonSpawner->spawnMonster();
    demon->show();

    auto sorcerer = sorcererSpawner->spawnMonster();
    sorcerer->show();

    std::cout << "DONE" << std::endl;

    return 0;
}
