#ifndef DUCKING_STATE_HPP
#define DUCKING_STATE_HPP

#include "heroine_state.hpp"
#include "input.hpp"

class Heroine;

class DuckingState : public HeroineState
{
    public:
    DuckingState(): chargeTime_(0) {}

    virtual HeroineState* handleInput(Heroine&, InputType);
    virtual void update(Heroine&);
    virtual void enter(Heroine&);

    private:
    int chargeTime_;
};

#endif // DUCKING_STATE_HPP
