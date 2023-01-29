#include <iostream>

#include "breed.hpp"
#include "monster.hpp"


int main()
{
    auto demon_type = Breed(nullptr, 10, "demon attack");
    auto demon = demon_type.newMonster();

    auto boss_type = Breed(&demon_type, 0, "boss demon attack");
    auto boss = boss_type.newMonster();

    std::cout << demon->getAttack() << std::endl;
    std::cout << boss->getAttack() << std::endl;

    std::cout << "DONE" << std::endl;
    return 0;
}
