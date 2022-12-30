#include<iostream>
#include "jump.hpp"
#include "actor.hpp"


void JumpCommand::execute(GameActor& actor) {
    actor.jump();
}
