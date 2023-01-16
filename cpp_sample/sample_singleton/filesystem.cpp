#include <iostream>
#include "filesystem.hpp"

FileSystem& FileSystem::instance() {
    static FileSystem *instance = new FileSystem();
    return *instance;
}


void FileSystem::show()
{
    std::cout << "file system" << std::endl;
}
