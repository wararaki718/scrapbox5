#ifndef WORLD_HPP
#define WORLD_HPP

#include <iostream>
#include "entity.hpp"

#define MAX_ENTITES 10


class World
{
public:
    World() {}
    ~World() {}
    void gameLoop();
    void add(Entity*);

private:
    Entity* entites_[MAX_ENTITES];
    int numEntites_{0};
};

#endif // WORLD_HPP
