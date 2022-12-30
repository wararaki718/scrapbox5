#include <iostream>
#include "actor.hpp"
#include "swap.hpp"


void SwapCommand::execute(GameActor& actor) {
    actor.swap();
}
