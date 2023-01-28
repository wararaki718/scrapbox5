#include <iostream>

#include "particle.hpp"
#include "particlesystem.hpp"
#include "sound.hpp"
#include "superpower.hpp"


void Superpower::move(double x, double y, double z)
{
    std::cout << x << ", " << y << ", " << z << std::endl;
}

void Superpower::playSound(SoundId sound)
{
    auto player = getSoundPlayer();
    player.setVolume(sound);
    player.playSound(sound);
    player.stopSound(sound);
}

void Superpower::spawnParticles(ParticleType type, int count)
{
    particles_->spawn(type, count);
}

double Superpower::getHeroX()
{
    return 2.0;
}

double Superpower::getHeroY()
{
    return 1.0;
}

double Superpower::getHeroZ()
{
    return 0.0;
}

SoundPlayer& Superpower::getSoundPlayer()
{
    return soundPlayer_;
}