#ifndef PARTICLE_POOL_HPP
#define PARTICLE_POOL_HPP

#include "particle.hpp"


class ParticlePool
{
    public:
    ParticlePool();
    void create(double, double, double, double, int);
    void animate();

    private:
    Particle* firstAvailable_;
    static const int POOL_SIZE = 100;
    Particle particles_[POOL_SIZE];
};

#endif // PARTICLE_POOL_HPP
