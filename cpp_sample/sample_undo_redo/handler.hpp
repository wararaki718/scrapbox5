#ifndef HANDLER_HPP
#define HANDLER_HPP

#include "command.hpp"
#include "button.hpp"
#include "unit.hpp"


class InputHandler
{
    public:
    Command* handleInput();
    void press(ButtonType);
    void select(Unit*);

    private:
    ButtonType pressed_button;
    Unit* selected_unit;
    Unit* getSelectedUnit();
    bool isPressed(ButtonType);
};

#endif // HANDLER_HPP
