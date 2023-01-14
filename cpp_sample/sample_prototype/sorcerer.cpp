#include <iostream>

#include "monster.hpp"
#include "sorcerer.hpp"


Monster* Sorcerer::clone()
{
    return new Sorcerer(health_, speed_);
}


void Sorcerer::show()
{
    std::cout << "sorcerer: (" << health_ << ", " << speed_ << ")" << std::endl;
}
