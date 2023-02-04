#ifndef CONTROLLER_HPP
#define CONTROLLER_HPP

#include "command.hpp"


class Controller
{
    public:
    static COMMAND getJoystickDirection()
    {
        return DIR_LEFT;
    }
};

#endif // CONTROLLER_HPP
