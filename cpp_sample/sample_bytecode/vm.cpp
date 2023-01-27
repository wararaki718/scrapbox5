#include "command.hpp"
#include "instruction.hpp"
#include "vm.hpp"


void VM::interpret(char bytecode[], int size)
{
    int amount, wizard, value;
    char instruction;
    
    for (int i = 0; i < size; i++)
    {
        instruction = bytecode[i];
        switch(instruction)
        {
            case INST_SET_HEALTH:
                amount = pop();
                wizard = pop();
                setHealth(wizard, amount);
                break;
            
            case INST_SET_WISDOM:
                amount = pop();
                wizard = pop();
                setWisdom(wizard, amount);
                break;
            
            case INST_SET_AGILITY:
                amount = pop();
                wizard = pop();
                setAgility(wizard, amount);
                break;
            
            case INST_PLAY_SOUND:
                playSound(pop());
                break;
            
            case INST_SPAWN_PARTICLES:
                spawnParticles(pop());
                break;
            
            case INST_LITERAL:
                value = bytecode[++i];
                push(value);
                break;
        }
    }
}


void VM::push(int value)
{
    stack_[stackSize_++] = value;
}


int VM::pop()
{
    return stack_[--stackSize_];
}
