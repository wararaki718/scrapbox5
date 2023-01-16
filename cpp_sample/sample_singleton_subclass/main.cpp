#include <iostream>
#include "wii.hpp"
#include "ps3.hpp"
#include "filesystem.hpp"


int main()
{
    auto system = FileSystem::instance();
    std::cout << "DONE" << std::endl;
    
    return 0;
}
