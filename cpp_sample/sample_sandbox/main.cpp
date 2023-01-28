#include <iostream>
#include "skylaunch.hpp"


int main()
{
    auto launch = SkyLaunch();
    launch.update();
    std::cout << "DONE" << std::endl;
    
    return 0;
}
