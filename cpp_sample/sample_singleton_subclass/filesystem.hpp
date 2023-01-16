#ifndef FILESYSTEM_HPP
#define FILESYSTEM_HPP

#include <string>


class FileSystem
{
    public:
    static FileSystem& instance();

    virtual ~FileSystem() = default;
    //virtual std::string read(std::string path) = 0;
    //virtual void write(std::string path, std::string text) = 0;

    protected:
    FileSystem() {}
};

#endif // FILESYSTEM_HPP
