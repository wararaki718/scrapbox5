#include "jumping_state.hpp"
#include "heroine.hpp"
#include "heroine_state.hpp"
#include "image.hpp"
#include "input.hpp"


void JumpingState::handleInput(Heroine& heroine, InputType input)
{
    if (input == InputType::DOWN) {
        heroine.state_ = &HeroineState::diving;
        heroine.setGraphic(ImageType::IMAGE_DIVE);
    }
}


void JumpingState::update(Heroine& heroine)
{
    return;
}
