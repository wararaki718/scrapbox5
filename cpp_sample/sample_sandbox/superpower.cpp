#include <iostream>

#include "particle.hpp"
#include "sound.hpp"
#include "superpower.hpp"


void Superpower::move(double x, double y, double z)
{
    std::cout << x << ", " << y << ", " << z << std::endl;
}

void Superpower::playSound(SoundId sound)
{
    switch (sound) {
        case BGM:
            std::cout << "bgm" << std::endl;
            break;

        case SOUND_SPROING:
            std::cout << "sproing" << std::endl;
            break;

        default:
            std::cout << "default sound" << std::endl;
            break;
    }
}

void Superpower::spawnParticles(ParticleType type, int count)
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

double Superpower::getHeroX()
{
    return 0.0;
}

double Superpower::getHeroY()
{
    return 1.0;
}

double Superpower::getHeroZ()
{
    return 2.0;
}
