#ifndef WORLD_HPP
#define WORLD_HPP

#include "volume.hpp"


class World
{
    public:
    World() {}
    void update();
    void resolveCollision(Volume, int, int, int);
};

#endif // WORLD_HPP
