#include<iostream>
#include "button.hpp"
#include "handler.hpp"
#include "unit.hpp"



int main() {
    // setup handler
    auto handler = new InputHandler();
    auto unit = new Unit();

    // user input
    auto buttons = {
        ButtonType::BUTTON_UP,
        ButtonType::BUTTON_DOWN,
        ButtonType::BUTTON_RIGHT,
        ButtonType::BUTTON_LEFT,
        ButtonType::BUTTON_NULL
    };

    handler->select(unit);
    for(auto button : buttons) {
        handler->press(button);
        auto command = handler->handleInput();
        if (command) {
            command->execute();
            command->undo();
        } else {
            std::cout << "null" << std::endl;
        }
    }
    
    std::cout << "DONE" << std::endl;
    return 0;
}
