#include <iostream>

#include "instruction.hpp"
#include "particle.hpp"
#include "sound.hpp"
#include "vm.hpp"


int main()
{
    auto vm = VM();
    char bytecode[] = {
        INST_LITERAL, 0,
        INST_LITERAL, 0,
        INST_GET_HEALTH,
        INST_LITERAL, 0,
        INST_GET_AGILITY,
        INST_LITERAL, 0,
        INST_GET_WISDOM,
        INST_ADD,
        INST_LITERAL, 2,
        INST_DIVIDE,
        INST_SET_HEALTH
    };
    int size = 16;

    vm.interpret(bytecode, size);
    std::cout << "DONE" << std::endl;

    return 0;
}
