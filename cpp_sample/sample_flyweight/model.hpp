#ifndef MODEL_HPP
#define MODEL_HPP

#include "mesh.hpp"
#include "texture.hpp"

class TreeModel
{
    public:
    TreeModel(): mesh_(Mesh::ROUGH), bark_(Texture::BROWN), leaves_(Texture::BROWN) {}
    TreeModel(Mesh mesh, Texture bark, Texture leaves): mesh_(mesh), bark_(bark), leaves_(leaves) {}

    private:
    Mesh mesh_;
    Texture bark_;
    Texture leaves_;
};

#endif // MODEL_HPP
