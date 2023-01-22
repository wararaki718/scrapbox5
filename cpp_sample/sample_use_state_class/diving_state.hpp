#ifndef DIVING_STATE_HPP
#define DIVING_STATE_HPP

#include "heroine_state.hpp"
#include "input.hpp"

class Heroine;

class DivingState : public HeroineState
{
    public:
    DivingState() {}

    virtual void handleInput(Heroine&, InputType);
    virtual void update(Heroine&);
};

#endif // DIVING_STATE_HPP
