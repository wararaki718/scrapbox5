#ifndef TREE_HPP
#define TREE_HPP

#include "model.hpp"
#include "position.hpp"
#include "color.hpp"


class Tree
{
    public:
    Tree(TreeModel* model): model_(model) {}
    Tree(TreeModel* model, Position position): model_(model), position_(position) {}
    Tree(
        TreeModel* model,
        Position position,
        double height,
        double tickness,
        Color barkTint,
        Color leafTint
    ): model_(model), position_(position), height_(height), tickness_(tickness), barkTint_(barkTint), leafTint_(leafTint) {}

    void show(void);

    private:
    TreeModel* model_;

    Position position_;
    double height_{0.0};
    double tickness_{0.0};
    Color barkTint_{Color::BRIGHT};
    Color leafTint_{Color::BRIGHT};
};

#endif // TREE_HPP