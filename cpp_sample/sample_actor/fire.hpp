#ifndef FIRE_HPP
#define FIRE_HPP

#include "actor.hpp"
#include "command.hpp"

class FireCommand : public Command
{
    public:
    void execute(GameActor& actor);
};

#endif // FIRE_HPP
