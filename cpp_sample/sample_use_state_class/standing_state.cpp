#include "ducking_state.hpp"
#include "jumping_state.hpp"
#include "heroine.hpp"
#include "heroine_state.hpp"
#include "image.hpp"
#include "input.hpp"
#include "standing_state.hpp"
#include "velocity.hpp"


HeroineState* StandingState::handleInput(Heroine& heroine, InputType input)
{
    if (input == InputType::B) {
        return new JumpingState();
    }

    if (input == InputType::DOWN) {
        return new DuckingState();
    }

    return nullptr;
}

void StandingState::enter(Heroine& heroine)
{
    heroine.setGraphic(ImageType::IMAGE_STAND);
}


void StandingState::update(Heroine& heroine)
{
    return;
}
