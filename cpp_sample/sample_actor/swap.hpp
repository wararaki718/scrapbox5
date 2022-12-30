#ifndef SWAP_HPP
#define SWAP_HPP

#include "actor.hpp"
#include "command.hpp"

class SwapCommand : public Command
{
    public:
    void execute(GameActor& actor);
};

#endif // SWAP_HPP
