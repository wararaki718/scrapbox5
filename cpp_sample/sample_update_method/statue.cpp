#include <iostream>

#include "statue.hpp"


void Statue::update()
{
    if (++frames_ == delay_)
    {
        shootLightning();
        frames_ = 0;
    }
    std::cout << "  statue update" << std::endl;
}


void Statue::shootLightning()
{
    std::cout << "shoot lightning" << std::endl;
}
