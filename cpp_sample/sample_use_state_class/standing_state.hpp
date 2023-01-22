#ifndef STANDING_STATE_HPP
#define STANDING_STATE_HPP

#include "heroine_state.hpp"
#include "input.hpp"
#include "velocity.hpp"

class Heroine;

class StandingState: public HeroineState
{
    public:
    StandingState() {}
    
    virtual void handleInput(Heroine&, InputType);
    virtual void update(Heroine&);

    private:
    int chargeTime_{0};
    int yVelocity_{STAND_VELOCITY};
};

#endif // STANDING_STATE_HPP
