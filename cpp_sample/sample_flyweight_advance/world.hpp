#ifndef WORLD_HPP
#define WORLD_HPP

#include "params.hpp"
#include "terrain.hpp"
#include "texture.hpp"


class World
{
    public:
    World(): grassTerrain_(1, false, Texture::GRASS), hillTerrain_(3, false, Texture::HILL), riverTerrian_(2, true, Texture::RIVER) {}

    void generateTerrain(void);
    const Terrain& getTile(int, int) const;

    private:
    Terrain grassTerrain_;
    Terrain hillTerrain_;
    Terrain riverTerrian_;

    Terrain* tiles_[WIDTH][HEIGHT];    
};

#endif // WORLD_HPP