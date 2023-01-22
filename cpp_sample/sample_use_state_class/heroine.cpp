#include <iostream>

#include "heroine.hpp"
#include "image.hpp"
#include "input.hpp"
#include "param.hpp"
#include "velocity.hpp"


void Heroine::handleInput(InputType input)
{
    state_->handleInput(*this, input);
}


void Heroine::update()
{
    state_->update(*this);
}


void Heroine::setGraphic(ImageType image)
{
    switch (image)
    {
    case ImageType::IMAGE_JUMP:
        std::cout << "jump image" << std::endl;
        break;
    case ImageType::IMAGE_STAND:
        std::cout << "stand image" << std::endl;
        break;
    case ImageType::IMAGE_DUCK:
        std::cout << "duck image" << std::endl;
        break;
    case ImageType::IMAGE_DIVE:
        std::cout << "dive image" << std::endl;
        break;
    default:
        break;
    }
}

void Heroine::superBomb()
{
    std::cout << "super bomb" << std::endl;
}
