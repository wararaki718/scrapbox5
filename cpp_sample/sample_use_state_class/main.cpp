#include <iostream>
#include <vector>

#include "input.hpp"
#include "heroine.hpp"


int main()
{
    auto heroine = Heroine();

    auto commands = std::vector<InputType>{
        InputType::B,
        InputType::DOWN,
        InputType::RELEASE_DOWN,
        InputType::B
    };

    for(auto command: commands) {
        heroine.handleInput(command);
        heroine.update();
    }

    std::cout << "DONE" << std::endl;
    return 0;
}
