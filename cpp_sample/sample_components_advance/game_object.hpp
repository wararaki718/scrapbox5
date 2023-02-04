#ifndef GAME_OBJECT_HPP
#define GAME_OBJECT_HPP


#include "graphics.hpp"
#include "graphics_component.hpp"
#include "input_component.hpp"
#include "physics_component.hpp"
#include "world.hpp"


class GameObject
{
    public:
    int velocity;
    int x, y;
    GameObject(
        InputComponent* input,
        PhysicsComponent* physics,
        GraphicsComponent* graphics
    ): input_(input), physics_(physics), graphics_(graphics) {}

    void update(World&, Graphics&);

    private:
    InputComponent* input_;
    PhysicsComponent* physics_;
    GraphicsComponent* graphics_;
};

#endif // GAME_OBJECT_HPP
