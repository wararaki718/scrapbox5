#include <iostream>

#include "demon.hpp"
#include "ghost.hpp"
#include "monster.hpp"
#include "sorcerer.hpp"
#include "spawner.hpp"


int main()
{
    Monster* ghostPrototype = new Ghost(15, 3);
    Spawner* ghostSpawner = new Spawner(ghostPrototype);

    Monster* demonPrototype = new Demon(1, 13);
    Spawner* demonSpawner = new Spawner(demonPrototype);

    Monster* sorcererPrototype = new Sorcerer(15, 33);
    Spawner* sorcererSpawner = new Spawner(sorcererPrototype);

    auto ghost = ghostSpawner->spawnMonster();
    ghost->show();

    auto demon = demonSpawner->spawnMonster();
    demon->show();

    auto sorcerer = sorcererSpawner->spawnMonster();
    sorcerer->show();

    std::cout << "DONE" << std::endl;

    return 0;
}
