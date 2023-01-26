#include "entity.hpp"
#include "world.hpp"


void World::gameLoop()
{
    int i = 0;
    while(i < 10)
    {
        std::cout << "user inputs" << std::endl;
        for (int i = 0; i < numEntites_; i++)
        {
            entites_[i]->update();
        }

        std::cout << "simulation" << std::endl;
        std::cout << "-----" << std::endl;
        i++;
    }
}


void World::add(Entity* entity)
{
    entites_[numEntites_] = entity;
    numEntites_++;
}
