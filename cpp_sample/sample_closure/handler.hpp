#ifndef HANDLER_HPP
#define HANDLER_HPP

#include <functional>
#include <map>
#include <string>
#include "button.hpp"
#include "unit.hpp"


class InputHandler
{
    public:
    std::map<std::string, std::function<void(void)>> handleInput();
    void press(ButtonType);
    void select(Unit*);

    private:
    ButtonType pressed_button;
    Unit* selected_unit;
    Unit* getSelectedUnit();
    bool isPressed(ButtonType);
};

#endif // HANDLER_HPP
