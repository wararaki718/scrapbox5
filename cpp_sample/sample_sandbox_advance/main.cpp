#include <iostream>

#include "particlesystem.hpp"
#include "skylaunch.hpp"


int main()
{
    auto particles = new ParticleSystem();
    auto launch = new SkyLaunch();
    launch->init(particles);
    launch->update();
    std::cout << "DONE" << std::endl;
    
    return 0;
}
