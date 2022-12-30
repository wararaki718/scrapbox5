#include "button.hpp"
#include "command.hpp"
#include "handler.hpp"
#include "fire.hpp"
#include "jump.hpp"
#include "lurch.hpp"
#include "swap.hpp"


Command* InputHandler::handleInput() {
    if (isPressed(ButtonType::BUTTON_X)) {
       return buttonX_;
    }
    else if (isPressed(ButtonType::BUTTON_Y)) {
        return buttonY_;
    }
    else if (isPressed(ButtonType::BUTTON_A)) {
        return buttonA_;
    }
    else if (isPressed(ButtonType::BUTTON_B)) {
        return buttonB_;
    }

    return nullptr;
}


void InputHandler::setButton() {
    buttonX_ = new JumpCommand();
    buttonY_ = new FireCommand();
    buttonA_ = new SwapCommand();
    buttonB_ = new LurchCommand();
}


bool InputHandler::isPressed(ButtonType button_type) {
    return pressed_button == button_type;
}


void InputHandler::press(ButtonType button_type) {
    pressed_button = button_type;
}
