#ifndef PARTICLE_SYSTEM_HPP
#define PARTICLE_SYSTEM_HPP

#include "particle.hpp"


class ParticleSystem
{
    public:
    ParticleSystem(): numActive_(0), numParticles_(0) {}

    void update();
    void addParticle(Particle);
    void activateParticle(int);
    void deactivateParticle(int);

    private:
    static const int MAX_PARTICLES = 100000;
    int numActive_;
    int numParticles_;
    Particle particles_[MAX_PARTICLES];
};

#endif // PARTICLE_SYSTEM_HPP
