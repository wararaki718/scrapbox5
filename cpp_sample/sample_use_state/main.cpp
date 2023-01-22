#include <iostream>
#include <vector>

#include "input.hpp"
#include "heroine.hpp"


int main()
{
    auto heroine = Heroine();

    auto commands = std::vector<InputType>{
        InputType::PRESS_B,
        InputType::PRESS_DOWN,
        InputType::PRESS_RELEASE_DOWN,
        InputType::PRESS_B
    };

    for(auto command: commands) {
        heroine.handleInput(command);
        heroine.update();
    }

    std::cout << "DONE" << std::endl;
    return 0;
}
