#include "particle_pool.hpp"


ParticlePool::ParticlePool()
{
    firstAvailable_ = &particles_[0];
    
    for (int i = 0; i < POOL_SIZE-1; i++)
    {
        particles_[i].setNext(&particles_[i+1]);
    }

    particles_[POOL_SIZE-1].setNext(nullptr);
}


void ParticlePool::animate()
{
    for(int i = 0; i < POOL_SIZE; i++)
    {
        if(particles_[i].animate())
        {
            particles_[i].setNext(firstAvailable_);
            firstAvailable_ = &particles_[i];
        }
    }
}


void ParticlePool::create(double x, double y, double xVel, double yVel, int lifetime)
{
    auto newParticle = firstAvailable_;
    firstAvailable_ = newParticle->getNext();

    newParticle->init(x, y, xVel, yVel, lifetime);
}
