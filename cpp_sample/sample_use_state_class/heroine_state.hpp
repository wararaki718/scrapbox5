#ifndef HEROINE_STATE_HPP
#define HEROINE_STATE_HPP

#include "input.hpp"
#include "standing_state.hpp"
#include "ducking_state.hpp"
#include "jumping_state.hpp"
#include "diving_state.hpp"

class Heroine;

class HeroineState
{
    public:
    static StandingState standing;
    static DuckingState ducking;
    static JumpingState jumping;
    static DivingState diving;

    virtual ~HeroineState() {}
    virtual void handleInput(Heroine&, InputType);

    virtual void update(Heroine&);
};

StandingState HeroineState::standing = StandingState();
DuckingState HeroineState::ducking = DuckingState();
JumpingState HeroineState::jumping = JumpingState();
DivingState HeroineState::diving = DivingState();


#endif //HEROINE_STATE_HPP
