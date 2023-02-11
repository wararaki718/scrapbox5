#include <iostream>

#include "particle.hpp"
#include "particle_system.hpp"

#define MAX_ENTITIES 10


int main()
{
    auto system = ParticleSystem();
    for (int i = 0; i < 5; i++) {
        auto particle = Particle();
        system.addParticle(particle);
        system.activateParticle(i);
    }
    
    int k = 4;
    while(k >= 0)
    {
        system.update();
        system.deactivateParticle(k);
        std::cout << std::endl;
        k--;
    }

    std::cout << "DONE" << std::endl;
    return 0;
}
