#include <iostream>

#include "breed.hpp"
#include "monster.hpp"


int main()
{
    auto demon_type = Breed(10, "demon attack");
    auto demon = Monster(demon_type);

    auto dragon_type = Breed(20, "dragon attack");
    auto dragon = Monster(dragon_type);

    std::cout << demon.getAttack() << std::endl;
    std::cout << dragon.getAttack() << std::endl;

    std::cout << "DONE" << std::endl;
    return 0;
}
