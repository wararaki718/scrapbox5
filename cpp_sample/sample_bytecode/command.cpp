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
