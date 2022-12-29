#include<iostream>
#include "button.hpp"
#include "handler.hpp"



int main() {
    // setup handler
    auto handler = new InputHandler();
    handler->setButton();

    // user input
    auto commands = {
        ButtonType::BUTTON_X,
        ButtonType::BUTTON_Y,
        ButtonType::BUTTON_A,
        ButtonType::BUTTON_B
    };

    for(auto command : commands) {
        handler->press(command);
        handler->handleInput();
    }
    
    std::cout << "DONE" << std::endl;
    return 0;
}
