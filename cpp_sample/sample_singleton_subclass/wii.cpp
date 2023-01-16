#include <iostream>
#include <string>
#include "wii.hpp"


std::string WiiFileSystem::read(std::string path)
{
    std::cout << "wii read" << std::endl;
    return "wii read";
}


void WiiFileSystem::write(std::string path, std::string text)
{
    std::cout << "wii write" << std::endl;
    std::cout << path << std::endl;
    std::cout << text << std::endl;
}
