#ifndef TERRAIN_HPP
#define TERRAIN_HPP

#include "texture.hpp"

class Terrain
{
    public:
    Terrain(
        int moveCost,
        bool isWater,
        Texture texture
    ) : moveCost_(moveCost), isWater_(isWater), texture_(texture) {}
    int getMoveCost() const;
    bool isWater() const;
    const Texture& getTexture() const;


    private:
    int moveCost_;
    bool isWater_;
    Texture texture_;
};

#endif // TERRAIN_HPP
