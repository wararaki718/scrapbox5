#include <iostream>
#include "filesystem.hpp"
#include "platform.hpp"
#include "ps3.hpp"
#include "wii.hpp"


FileSystem& FileSystem::instance() {
#if PLATFORM == PS3
    static FileSystem *instance = new PS3FileSystem();
#elif PLATFORM == WII
    static FileSystem *instance = new WiiFileSystem();
#endif
    return *instance;
}
