#include <iostream>
#include "actor.hpp"



void GameActor::jump()
{
    std::cout << name << " jump" << std::endl;
}

void GameActor::fire()
{
    std::cout << name << " fire" << std::endl;
}

void GameActor::lurch()
{
    std::cout << name << " lurch" << std::endl;
}

void GameActor::swap()
{
    std::cout << name << " swap" << std::endl;
}
