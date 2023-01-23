#include "buffer.hpp"
#include "scene.hpp"


void Scene::draw()
{
    next_->clear();
    next_->draw(1, 1);
    next_->draw(4, 1);
    next_->draw(1, 3);
    next_->draw(2, 4);
    next_->draw(3, 4);
    next_->draw(4, 3);
    swap();
}


Framebuffer& Scene::getBuffer()
{
    return *current_;
}


void Scene::swap()
{
    auto temp = current_;
    current_ = next_;
    next_ = temp;
}
