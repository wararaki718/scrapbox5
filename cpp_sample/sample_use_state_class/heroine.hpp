#ifndef HEROINE_HPP
#define HEROINE_HPP

#include "heroine_state.hpp"
#include "image.hpp"
#include "input.hpp"
#include "standing_state.hpp"

class Heroine
{
    public:
    Heroine() {
        state_ = new StandingState();
    }
    virtual void handleInput(InputType);
    virtual void update();
    void setGraphic(ImageType);
    void superBomb();
    HeroineState* state_;
};

#endif // HEROINE_HPP
