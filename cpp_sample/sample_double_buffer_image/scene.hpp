#ifndef SCENE_HPP
#define SCENE_HPP

#include "buffer.hpp"

class Scene
{
    public:
    Scene(): current_(&buffers_[0]), next_(&buffers_[1]) {}

    void draw();
    Framebuffer& getBuffer();
    
    private:
    void swap();

    Framebuffer buffers_[2];
    Framebuffer* current_;
    Framebuffer* next_;
};

#endif // SCENE_HPP
