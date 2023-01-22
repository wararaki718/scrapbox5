#include <iostream>

#include "ducking_state.hpp"
#include "heroine.hpp"
#include "heroine_state.hpp"
#include "image.hpp"
#include "input.hpp"
#include "param.hpp"
#include "standing_state.hpp"


HeroineState* DuckingState::handleInput(Heroine& heroine, InputType input)
{
    if (input == InputType::RELEASE_DOWN) {
        return new StandingState();
    }

    return nullptr;
}


void DuckingState::enter(Heroine& heroine)
{
    heroine.setGraphic(ImageType::IMAGE_DUCK);
}


void DuckingState::update(Heroine& heroine)
{
    chargeTime_++;
    if(chargeTime_ > MAX_CHARGE) {
        heroine.superBomb();
    }
}
