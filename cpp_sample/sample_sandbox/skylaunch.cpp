#include "particle.hpp"
#include "skylaunch.hpp"
#include "sound.hpp"


void SkyLaunch::update()
{
    activate();
}

void SkyLaunch::activate()
{
    if(getHeroZ() == 0) {
        move(0, 0, 20);
        playSound(SOUND_SPROING);
        spawnParticles(PARTICLE_DUST, 10);
    }
    else if (getHeroZ() < 10.0f) {
        playSound(SOUND_SWOOP);
        move(0, 0, getHeroZ() - 20);
    }
    else {
        playSound(SOUND_DIVE);
        spawnParticles(PARTICLE_SPARKLES, 1);
        move(0, 0, -getHeroZ());
    }
}
