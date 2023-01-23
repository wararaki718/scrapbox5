#include "buffer.hpp"
#include "color.hpp"


void Framebuffer::clear()
{
    for (int i = 0; i < WIDTH * HEIGHT; i++) {
        pixels_[i] = WHITE;
    }
}


void Framebuffer::draw(int x, int y)
{
    pixels_[(WIDTH*y) + x] = BLACK;
}


char* Framebuffer::getPixels()
{
    return pixels_;
}
