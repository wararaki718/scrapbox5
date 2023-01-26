#include <iostream>

#include "skeleton.hpp"


void Skeleton::update()
{
    if (patrollingLeft_)
    {
        setX(x() - 1);
        if (x() == 0) {
            patrollingLeft_ = false;
        }
    }
    else
    {
        setX(x() + 1);
        if (x() == 100) {
            patrollingLeft_ = true;
        }
    }

    std::cout << "  skeleton update" << std::endl;
}
