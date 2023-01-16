#include <iostream>
#include "filesystem.hpp"


int main()
{
    auto system = FileSystem::instance();
    system.show();

    std::cout << "DONE" << std::endl;
    
    return 0;
}
