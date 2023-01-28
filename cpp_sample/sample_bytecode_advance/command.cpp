#include <iostream>

#include "command.hpp"


void setHealth(int wizard, int amount)
{
    std::cout << "health: (" << wizard << ", " << amount << ")" << std::endl;
}

void setWisdom(int wizard, int amount)
{
    std::cout << "wisdom: (" << wizard << ", " << amount << ")" << std::endl;
}

void setAgility(int wizard, int amount)
{
    std::cout << "agility: (" << wizard << ", " << amount << ")" << std::endl;
}

void playSound(int soundId)
{
    std::cout << "play sound: " << soundId << std::endl;
}

void spawnParticles(int particleType)
{
    std::cout << "particle type: " << particleType << std::endl;
}

int getHealth(int wizard)
{
    if(wizard == 0) {
        return 45;
    }
    return 10;
}

int getWisdom(int wizard)
{
    if(wizard == 0) {
        return 11;
    }
    return 10;
}

int getAgility(int wizard)
{
    if(wizard == 0) {
        return 7;
    }
    return 10;
}
