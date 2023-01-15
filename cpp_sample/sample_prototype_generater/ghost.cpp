#include <iostream>

#include "ghost.hpp"
#include "monster.hpp"


Monster* Ghost::clone()
{
    return new Ghost(health_, speed_);
}


void Ghost::show()
{
    std::cout << "ghost: (" << health_ << ", " << speed_ << ")" << std::endl;
}
