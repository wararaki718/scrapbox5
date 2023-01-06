#include <iostream>

#include "model.hpp"
#include "position.hpp"
#include "tree.hpp"


int main()
{
    TreeModel* model = new TreeModel();
    Tree tree1 = Tree(model);
    Position position = Position(1, 1, 1);
    Tree tree2 = Tree(model, position);

    tree1.show();
    tree2.show();

    std::cout << "DONE" << std::endl;
    return 0;
}
