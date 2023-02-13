#include <iostream>
#include "particle_pool.hpp"


int main()
{
    auto pool = ParticlePool();
    pool.create(1, 1, 1, 1, 2);
    pool.animate();
    std::cout << "DONE" << std::endl;
    return 0;
}
