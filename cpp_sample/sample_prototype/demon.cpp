#include <iostream>

#include "demon.hpp"
#include "monster.hpp"


Monster* Demon::clone()
{
    return new Demon(health_, speed_);
}

void Demon::show()
{
    std::cout << "demon: (" << health_ << ", " << speed_ << ")" << std::endl;
}
