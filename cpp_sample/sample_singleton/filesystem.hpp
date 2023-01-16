#ifndef FILESYSTEM_HPP
#define FILESYSTEM_HPP

class FileSystem
{
    public:
    static FileSystem& instance();
    void show();

    private:
    FileSystem() {}
};

#endif // FILESYSTEM_HPP
