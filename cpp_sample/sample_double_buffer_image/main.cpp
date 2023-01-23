#include <iostream>

#include "buffer.hpp"
#include "scene.hpp"


int main()
{
    auto scene = Scene();
    scene.draw();
    scene.draw();
    auto pixels = scene.getBuffer().getPixels();
    std::cout << *pixels << std::endl;
    std::cout << "DONE" << std::endl;
    return 0;
}
