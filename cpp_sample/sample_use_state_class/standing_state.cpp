#include "standing_state.hpp"
#include "heroine.hpp"
#include "heroine_state.hpp"
#include "image.hpp"
#include "input.hpp"
#include "velocity.hpp"


void StandingState::handleInput(Heroine& heroine, InputType input)
{
    if (input == InputType::B) {
        heroine.state_ = &HeroineState::jumping;
        heroine.setGraphic(ImageType::IMAGE_JUMP);
        return;
    }

    if (input == InputType::DOWN) {
        heroine.state_ = &HeroineState::ducking;
        heroine.setGraphic(ImageType::IMAGE_DUCK);
        return;
    }
}


void StandingState::update(Heroine& heroine)
{
    return;
}
