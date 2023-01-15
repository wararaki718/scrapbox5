#include <iostream>

#include "sorcerer.hpp"


void Sorcerer::show()
{
    std::cout << "sorcerer: (" << health_ << ", " << speed_ << ")" << std::endl;
}
