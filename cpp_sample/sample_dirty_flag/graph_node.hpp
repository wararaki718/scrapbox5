#ifndef GRAPH_NODE_HPP
#define GRAPH_NODE_HPP

#include "mesh.hpp"
#include "transform.hpp"

class GraphNode
{
    public:
    GraphNode(Mesh* mesh): mesh_(mesh), local_(Transform::origin()) {}
    void render(Transform, bool);
    void setTransform(Transform);

    private:
    Transform local_;
    Mesh* mesh_;

    static const int MAX_CHILDREN = 1000;
    GraphNode* children_[MAX_CHILDREN];
    int numChildren_;

    Transform world_;
    bool dirty_{true};

    void renderMesh(Mesh*, Transform);
};

#endif // GRAPH_NODE_HPP
