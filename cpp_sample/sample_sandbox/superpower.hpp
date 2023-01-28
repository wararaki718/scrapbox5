#ifndef SUPERPOWER_HPP
#define SUPERPOWER_HPP

#include "particle.hpp"
#include "sound.hpp"

class Superpower
{
    public:
    virtual ~Superpower() {}

    protected:
    virtual void activate() = 0;
    double getHeroX();
    double getHeroY();
    double getHeroZ();

    void move(double, double, double);
    void playSound(SoundId);
    void spawnParticles(ParticleType, int);
};

#endif // SUPERPOWER_HPP
