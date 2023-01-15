#include <iostream>

#include "demon.hpp"
#include "ghost.hpp"
#include "sorcerer.hpp"
#include "spawner.hpp"


int main()
{
    Spawner* ghostSpawner = new SpawnerFor<Ghost>();
    Spawner* demonSpawner = new SpawnerFor<Demon>();
    Spawner* sorcererSpawner = new SpawnerFor<Sorcerer>();

    auto ghost = ghostSpawner->spawnMonster();
    ghost->show();

    auto demon = demonSpawner->spawnMonster();
    demon->show();

    auto sorcerer = sorcererSpawner->spawnMonster();
    sorcerer->show();

    std::cout << "DONE" << std::endl;

    return 0;
}
