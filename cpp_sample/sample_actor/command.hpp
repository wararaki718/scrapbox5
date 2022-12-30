#ifndef COMMAND_HPP
#define COMMAND_HPP

#include "actor.hpp"


class Command
{
    public:
    virtual ~Command() {}
    virtual void execute(GameActor& actor) = 0;
};

#endif // COMMAND_HPP