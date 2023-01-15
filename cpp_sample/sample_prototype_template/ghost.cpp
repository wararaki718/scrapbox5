#include <iostream>

#include "ghost.hpp"


void Ghost::show()
{
    std::cout << "ghost: (" << health_ << ", " << speed_ << ")" << std::endl;
}
