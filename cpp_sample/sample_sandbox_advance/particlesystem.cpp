#include <iostream>

#include "particle.hpp"
#include "particlesystem.hpp"

void ParticleSystem::spawn(ParticleType type, int count)
{
    switch (type)
    {
    case PARTICLE_FRAME:
        std::cout << "particle frame: " << count << std::endl;
        break;
    
    case PARTICLE_DUST:
        std::cout << "particle dust: " << count << std::endl;
        break;

    default:
        std::cout << "default particle: " << count << std::endl;
        break;
    }
}