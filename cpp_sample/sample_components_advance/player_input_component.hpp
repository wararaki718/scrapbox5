#ifndef PLAYER_INPUT_COMPONENT_HPP
#define PLAYER_INPUT_COMPONENT_HPP

#include "input_component.hpp"

class GameObject;

class PlayerInputComponent: public InputComponent
{
    public:
    void update(GameObject&);

    private:
    static const int WALK_ACCELERATION = 1;
};

#endif // PLAYER_INPUT_COMPONENT_HPP
