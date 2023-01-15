#include <iostream>

#include "demon.hpp"


void Demon::show()
{
    std::cout << "demon: (" << health_ << ", " << speed_ << ")" << std::endl;
}
