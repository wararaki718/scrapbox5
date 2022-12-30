#include <iostream>
#include "actor.hpp"
#include "lurch.hpp"


void LurchCommand::execute(GameActor& actor) {
    actor.lurch();
}
