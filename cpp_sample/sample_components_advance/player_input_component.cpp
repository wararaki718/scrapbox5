#include "command.hpp"
#include "controller.hpp"
#include "game_object.hpp"
#include "player_input_component.hpp"


void PlayerInputComponent::update(GameObject& obj)
{
    switch (Controller::getJoystickDirection())
    {
    case DIR_LEFT:
        obj.velocity -= WALK_ACCELERATION;
        break;
    
    case DIR_RIGHT:
        obj.velocity += WALK_ACCELERATION;
        break;
    }
}
