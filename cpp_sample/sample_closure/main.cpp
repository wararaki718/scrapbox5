#include<iostream>
#include "button.hpp"
#include "handler.hpp"
#include "unit.hpp"


int main() {
    // setup handler
    auto handler = new InputHandler();
    auto unit = new Unit(0, 0);
    auto unit2 = new Unit(0, 0);

    // user input
    auto buttons = {
        ButtonType::BUTTON_UP,
        ButtonType::BUTTON_DOWN,
        ButtonType::BUTTON_RIGHT,
        ButtonType::BUTTON_LEFT,
        ButtonType::BUTTON_NULL
    };

    std::cout << "execute" << std::endl;
    handler->select(unit);
    for(auto button : buttons) {
        handler->press(button);
        auto command = handler->handleInput();
        if (!command.empty()) {
            command["execute"]();
        } else {
            std::cout << "null" << std::endl;
        }
    }
    std::cout << std::endl;

    std::cout << "execute + undo" << std::endl;
    handler->select(unit2);
    for(auto button : buttons) {
        handler->press(button);
        auto command = handler->handleInput();
        if (!command.empty()) {
            command["execute"]();
            command["undo"]();
        } else {
            std::cout << "null" << std::endl;
        }
    }
    std::cout << std::endl;
    
    std::cout << "DONE" << std::endl;
    return 0;
}
