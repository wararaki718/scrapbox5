#include <iostream>
#include <string>
#include "ps3.hpp"


std::string PS3FileSystem::read(std::string path)
{
    std::cout << "ps3 read" << std::endl;
    return "ps3 read";
}


void PS3FileSystem::write(std::string path, std::string text)
{
    std::cout << "ps3 write" << std::endl;
    std::cout << path << std::endl;
    std::cout << text << std::endl;
}
