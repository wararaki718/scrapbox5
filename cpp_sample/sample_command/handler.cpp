#include "button.hpp"
#include "handler.hpp"
#include "fire.hpp"
#include "jump.hpp"
#include "lurch.hpp"
#include "swap.hpp"


void InputHandler::handleInput() {
    if (isPressed(ButtonType::BUTTON_X)) {
        buttonX_->execute();
    }
    else if (isPressed(ButtonType::BUTTON_Y)) {
        buttonY_->execute();
    }
    else if (isPressed(ButtonType::BUTTON_A)) {
        buttonA_->execute();
    }
    else if (isPressed(ButtonType::BUTTON_B)) {
        buttonB_->execute();
    }
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
