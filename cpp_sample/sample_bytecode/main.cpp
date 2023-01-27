#include <iostream>

#include "instruction.hpp"
#include "particle.hpp"
#include "sound.hpp"
#include "vm.hpp"


int main()
{
    auto vm = VM();
    char bytecode[] = {
        INST_LITERAL, 1,
        INST_LITERAL, 10,
        INST_SET_HEALTH,
        INST_LITERAL, 2,
        INST_LITERAL, 20,
        INST_SET_WISDOM,
        INST_LITERAL, 3,
        INST_LITERAL, 30,
        INST_SET_AGILITY,
        INST_LITERAL, SOUND_BANG,
        INST_PLAY_SOUND,
        INST_LITERAL, PARTICLE_FRAME,
        INST_SPAWN_PARTICLES
    };
    int size = 21;

    vm.interpret(bytecode, size);
    std::cout << "DONE" << std::endl;

    return 0;
}
