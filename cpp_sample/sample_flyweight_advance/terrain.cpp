#include "terrain.hpp"
#include "texture.hpp"


int Terrain::getMoveCost() const {
    return moveCost_;
}


bool Terrain::isWater() const {
    return isWater_;
}


const Texture& Terrain::getTexture() const {
    return texture_;
}
