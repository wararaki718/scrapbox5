#include <iostream>
#include "actor.hpp"
#include "fire.hpp"


void FireCommand::execute(GameActor& actor) {
    actor.fire();
}
