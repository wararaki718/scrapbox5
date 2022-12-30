#ifndef LURCH_HPP
#define LURCH_HPP

#include "actor.hpp"
#include "command.hpp"

class LurchCommand : public Command
{
    public:
    void execute(GameActor& actor);
};

#endif // LURCH_HPP
