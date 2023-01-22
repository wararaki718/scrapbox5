#include <iostream>

#include "heroine.hpp"
#include "image.hpp"
#include "input.hpp"
#include "param.hpp"
#include "state.hpp"
#include "velocity.hpp"


void Heroine::handleInput(InputType input)
{
    switch (state_)
    {
    case State::STATE_STANDING:
        if (input == InputType::PRESS_B) {
            state_ = State::STATE_JUMPING;
            yVelocity_ = JUMP_VELOCITY;
            setGraphic(ImageType::IMAGE_JUMP);
        }
        else if (input == InputType::PRESS_DOWN) {
            state_ = State::STATE_DUCKING;
            chargeTime_ = 0;
            setGraphic(ImageType::IMAGE_DUCK);
        }
        else {
            std::cout << "skip standing" << std::endl;
        }
        break;

    case State::STATE_JUMPING:
        if (input == InputType::PRESS_DOWN) {
            state_ = State::STATE_DIVING;
            setGraphic(ImageType::IMAGE_DIVE);
        }
        else {
            std::cout << "skip jumping" << std::endl;
        }
        break;
    
    case State::STATE_DUCKING:
        if (input == InputType::PRESS_RELEASE_DOWN) {
            state_ = State::STATE_STANDING;
            setGraphic(ImageType::IMAGE_STAND);
        }
        else {
            std::cout << "skip ducking" << std::endl;
        }
        break;

    default:
        break;
    }
}


void Heroine::update()
{
    if (state_ == State::STATE_DUCKING) {
        chargeTime_++;
        if (chargeTime_ > MAX_CHARGE) {
            superBomb();
        }
    }
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
