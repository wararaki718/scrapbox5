#ifndef BUFFER_HPP
#define BUFFER_HPP

class Framebuffer
{
    public:
    Framebuffer() {}
    void clear();
    void draw(int, int);
    char* getPixels();

    private:
    static const int WIDTH = 5;
    static const int HEIGHT = 5;
    char pixels_[WIDTH * HEIGHT];
};

#endif // BUFFER_HPP
