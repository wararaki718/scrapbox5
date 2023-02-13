#include "particle_pool.hpp"


void ParticlePool::animate()
{
    for(int i = 0; i < POOL_SIZE; i++)
    {
        particles_[i].animate();
    }
}


void ParticlePool::create(double x, double y, double xVel, double yVel, int lifetime)
{
    for(int i = 0; i < POOL_SIZE; i++)
    {
        if(!particles_[i].inUse())
        {
            particles_[i].init(x, y, xVel, yVel, lifetime);
            return;
        }
    }
}