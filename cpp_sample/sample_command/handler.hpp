#ifndef HANDLER_HPP
#define HANDLER_HPP

#include "command.hpp"
#include "button.hpp"


class InputHandler
{
    public:
    void handleInput();
    void setButton();
    bool isPressed(ButtonType);
    void press(ButtonType);

    private:
    Command* buttonX_;
    Command* buttonY_;
    Command* buttonA_;
    Command* buttonB_;
    ButtonType pressed_button;
};

#endif // HANDLER_HPP
