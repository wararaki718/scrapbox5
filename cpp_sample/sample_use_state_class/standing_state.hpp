#ifndef STANDING_STATE_HPP
#define STANDING_STATE_HPP

#include "heroine_state.hpp"
#include "input.hpp"

class Heroine;

class StandingState: public HeroineState
{
    public:
    StandingState() {}
    
    virtual HeroineState* handleInput(Heroine&, InputType);
    virtual void update(Heroine&);
    virtual void enter(Heroine&);
};

#endif // STANDING_STATE_HPP
