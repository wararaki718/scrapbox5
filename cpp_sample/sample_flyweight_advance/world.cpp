#include <cstdlib>

#include "params.hpp"
#include "terrain.hpp"
#include "world.hpp"


void World::generateTerrain()
{
    srand(1000);
    for(int x = 0; x < WIDTH; x++) {
        for(int y = 0; y < HEIGHT; y++) {
            if(rand()%10 == 0) {
                tiles_[x][y] = &hillTerrain_;
            } else {
                tiles_[x][y] = &grassTerrain_;
            }
        }
    }

    int x = rand() % WIDTH;
    for(int y = 0; y < HEIGHT; y++) {
        tiles_[x][y] = &riverTerrian_;
    }
}


const Terrain& World::getTile(int x, int y) const
{
    return *tiles_[x][y];
}
