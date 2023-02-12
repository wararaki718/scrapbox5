#include <iostream>

#include "graph_node.hpp"
#include "transform.hpp"


int main()
{
    auto graph = new GraphNode(nullptr);
    graph->setTransform(Transform::origin());
    graph->render(Transform::origin(), true);

    std::cout << "DONE" << std::endl;
    return 0;
}
