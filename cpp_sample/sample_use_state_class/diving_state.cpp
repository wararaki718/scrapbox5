#include <iostream>

#include "diving_state.hpp"
#include "heroine.hpp"
#include "input.hpp"


HeroineState* DivingState::handleInput(Heroine& heroine, InputType input)
{
    return nullptr;
}


void DivingState::enter(Heroine& heroine)
{
    heroine.setGraphic(ImageType::IMAGE_DIVE);
}


void DivingState::update(Heroine& heroine)
{
    return;
}
