#ifndef JUMP_HPP
#define JUMP_HPP

#include "actor.hpp"
#include "command.hpp"


class JumpCommand : public Command
{
    public:
    void execute(GameActor& actor);
};

#endif //JUMP_HPP
