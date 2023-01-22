#ifndef HEROINE_STATE_HPP
#define HEROINE_STATE_HPP

#include "input.hpp"

class Heroine;

class HeroineState
{
    public:
    virtual ~HeroineState() {}
    virtual HeroineState* handleInput(Heroine&, InputType);
    virtual void enter(Heroine&);
    virtual void update(Heroine&);
};

#endif //HEROINE_STATE_HPP
