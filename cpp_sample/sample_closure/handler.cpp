#include <functional>
#include <map>
#include <string>
#include "button.hpp"
#include "handler.hpp"
#include "move.hpp"


std::map<std::string, std::function<void(void)>> InputHandler::handleInput() {
    auto unit = getSelectedUnit();

    if (isPressed(ButtonType::BUTTON_UP)) {
        int destY = unit->y() - 1;
        return makeMoveUnitCommand(unit, unit->x(), destY);
    }
    if (isPressed(ButtonType::BUTTON_DOWN)) {
        int destY = unit->y() + 1;
        return makeMoveUnitCommand(unit, unit->x(), destY);
    }
    if (isPressed(ButtonType::BUTTON_RIGHT)) {
        int destX = unit->x() + 1;
        return makeMoveUnitCommand(unit, destX, unit->y());
    }
    if (isPressed(ButtonType::BUTTON_LEFT)) {
        int destX = unit->x() - 1;
        return makeMoveUnitCommand(unit, destX, unit->y());
    }

    std::map<std::string, std::function<void(void)>> empty;
    return empty;
}


bool InputHandler::isPressed(ButtonType button_type) {
    return pressed_button == button_type;
}


void InputHandler::press(ButtonType button_type) {
    pressed_button = button_type;
}


void InputHandler::select(Unit* unit) {
    selected_unit = unit;
}


Unit* InputHandler::getSelectedUnit() {
    return selected_unit;
}