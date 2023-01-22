#ifndef JUMPING_STATE_HPP
#define JUMPING_STATE_HPP

#include "heroine_state.hpp"
#include "input.hpp"

class Heroine;

class JumpingState: public HeroineState
{
    public:
    JumpingState() {}

    virtual HeroineState* handleInput(Heroine&, InputType);
    virtual void update(Heroine&);
    virtual void enter(Heroine&);
};

#endif // JUMPING_STATE_HPP
