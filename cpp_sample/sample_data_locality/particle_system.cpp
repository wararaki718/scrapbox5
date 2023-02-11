#include "particle.hpp"
#include "particle_system.hpp"


void ParticleSystem::update()
{
    for (int i = 0; i < numActive_; i++)
    {
        particles_[i].update();
    }
}


void ParticleSystem::activateParticle(int index)
{
    auto tmp = particles_[numActive_];
    particles_[numActive_] = particles_[index];
    particles_[index] = tmp;

    numActive_++;
}


void ParticleSystem::deactivateParticle(int index)
{
    numActive_--;
    auto tmp = particles_[numActive_];
    particles_[numActive_] = particles_[index];
    particles_[index] = tmp;
}
