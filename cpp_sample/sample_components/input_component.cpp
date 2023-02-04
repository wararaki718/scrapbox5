#include "bjorn.hpp"
#include "command.hpp"
#include "controller.hpp"
#include "input_component.hpp"


void InputComponent::update(Bjorn& bjorn)
{
    switch (Controller::getJoystickDirection())
    {
    case DIR_LEFT:
        bjorn.velocity -= WALK_ACCELERATION;
        break;
    
    case DIR_RIGHT:
        bjorn.velocity += WALK_ACCELERATION;
        break;
    }
}
