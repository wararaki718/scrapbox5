#ifndef DUCKING_STATE_HPP
#define DUCKING_STATE_HPP

#include "input.hpp"

class Heroine;
class HeroineState;

class DuckingState : public HeroineState
{
    public:
    DuckingState(): chargeTime_(0) {}

    virtual void handleInput(Heroine&, InputType);
    virtual void update(Heroine&);

    private:
    int chargeTime_;
};

#endif // DUCKING_STATE_HPP
