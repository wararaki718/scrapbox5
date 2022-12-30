#include<iostream>
#include "actor.hpp"
#include "button.hpp"
#include "handler.hpp"



int main() {
    // setup handler
    auto handler = new InputHandler();
    handler->setButton();

    // user input
    auto buttons = {
        ButtonType::BUTTON_X,
        ButtonType::BUTTON_Y,
        ButtonType::BUTTON_A,
        ButtonType::BUTTON_B
    };

    auto player = GameActor("player");
    auto cpu = GameActor("cpu");

    for(auto button : buttons) {
        handler->press(button);
        auto command = handler->handleInput();
        if (command) {
            command->execute(player);
        }
    }

    for(auto button : buttons) {
        handler->press(button);
        auto command = handler->handleInput();
        if (command) {
            command->execute(cpu);
        }
    }
    
    std::cout << "DONE" << std::endl;
    return 0;
}
