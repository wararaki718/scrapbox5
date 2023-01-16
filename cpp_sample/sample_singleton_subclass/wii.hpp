#ifndef WII_HPP
#define WII_HPP

#include <string>
#include "filesystem.hpp"

class WiiFileSystem: public FileSystem
{
    public:
    virtual std::string read(std::string path);
    virtual void write(std::string path, std::string text);
};

#endif // WII_HPP
