#include <iostream>

#include "ducking_state.hpp"
#include "heroine.hpp"
#include "heroine_state.hpp"
#include "image.hpp"
#include "input.hpp"
#include "param.hpp"


void DuckingState::handleInput(Heroine& heroine, InputType input)
{
    if (input == InputType::RELEASE_DOWN) {
        heroine.state_ = &HeroineState::standing;
        heroine.setGraphic(ImageType::IMAGE_STAND);
    }
}


void DuckingState::update(Heroine& heroine)
{
    chargeTime_++;
    if(chargeTime_ > MAX_CHARGE) {
        heroine.superBomb();
    }
}
