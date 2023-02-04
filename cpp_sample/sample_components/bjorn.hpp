#ifndef BJORN_HPP
#define BJORN_HPP

#include "graphics.hpp"
#include "world.hpp"
#include "graphics_component.hpp"
#include "input_component.hpp"
#include "physics_component.hpp"


class Bjorn
{
    public:
    Bjorn(): velocity(0), x(0), y(0) {
        input_ = InputComponent();
        pyhsics_ = PhysicsComponent();
        graphics_ = GraphicsComponent();
    }

    void update(World&, Graphics&);

    int velocity;
    int x;
    int y;

    private:
    InputComponent input_;
    PhysicsComponent pyhsics_;
    GraphicsComponent graphics_;
};

#endif // BJORN_HPP
