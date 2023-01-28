#ifndef SUPERPOWER_HPP
#define SUPERPOWER_HPP

#include "particle.hpp"
#include "particlesystem.hpp"
#include "sound.hpp"
#include "soundplayer.hpp"

class Superpower
{
    public:
    Superpower() {
        soundPlayer_ = SoundPlayer();
    }
    virtual ~Superpower() {}
    void init(ParticleSystem* particles) {
        particles_ = particles;
    }

    protected:
    virtual void activate() = 0;
    double getHeroX();
    double getHeroY();
    double getHeroZ();

    void move(double, double, double);
    void playSound(SoundId);
    void spawnParticles(ParticleType, int);
    SoundPlayer& getSoundPlayer();

    private:
    SoundPlayer soundPlayer_;
    ParticleSystem* particles_;
};

#endif // SUPERPOWER_HPP
