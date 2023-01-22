#ifndef JUMPING_STATE_HPP
#define JUMPING_STATE_HPP

#include "heroine_state.hpp"
#include "input.hpp"

class Heroine;

class JumpingState: public HeroineState
{
    public:
    JumpingState() {}

    virtual void handleInput(Heroine&, InputType);
    virtual void update(Heroine&);
};

#endif // JUMPING_STATE_HPP
