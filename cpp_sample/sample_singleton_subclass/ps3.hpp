#ifndef PS3_HPP
#define PS3_HPP

#include <string>
#include "filesystem.hpp"

class PS3FileSystem: public FileSystem
{
    public:
    virtual std::string read(std::string path);
    virtual void write(std::string path, std::string text);
};

#endif // PS3_HPP
