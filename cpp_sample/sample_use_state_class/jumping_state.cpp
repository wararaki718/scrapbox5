#include "diving_state.hpp"
#include "jumping_state.hpp"
#include "heroine.hpp"
#include "heroine_state.hpp"
#include "image.hpp"
#include "input.hpp"


HeroineState* JumpingState::handleInput(Heroine& heroine, InputType input)
{
    if (input == InputType::DOWN) {
        return new DivingState();
    }

    return nullptr;
}


void JumpingState::enter(Heroine& heroine)
{
    heroine.setGraphic(ImageType::IMAGE_JUMP);
}


void JumpingState::update(Heroine& heroine)
{
    return;
}
