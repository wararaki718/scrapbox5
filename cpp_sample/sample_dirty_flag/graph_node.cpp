#include <iostream>

#include "graph_node.hpp"


void GraphNode::render(Transform parentWorld, bool dirty)
{
    dirty_ |= dirty;
    if(dirty) {
        world_ = local_.combine(parentWorld);
        dirty_ = false;
    }

    if (mesh_) {
        renderMesh(mesh_, world_);
    }

    for (int i = 0; i < numChildren_; i++)
    {
        children_[i]->render(world_, dirty);
    }
    
    std::cout << "graph node render" << std::endl;
}


void GraphNode::renderMesh(Mesh* mesh, Transform transform)
{
    std::cout << "graph node render mesh" << std::endl;
}


void GraphNode::setTransform(Transform local)
{
    local_ = local;
    dirty_ = true;
}
