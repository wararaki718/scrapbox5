#include "button.hpp"
#include "handler.hpp"
#include "move.hpp"


Command* InputHandler::handleInput() {
    auto unit = getSelectedUnit();

    if (isPressed(ButtonType::BUTTON_UP)) {
        int destY = unit->y() - 1;
        return new MoveUnitCommand(unit, unit->x(), destY);
    }
    if (isPressed(ButtonType::BUTTON_DOWN)) {
        int destY = unit->y() + 1;
        return new MoveUnitCommand(unit, unit->x(), destY);
    }
    if (isPressed(ButtonType::BUTTON_RIGHT)) {
        int destX = unit->x() + 1;
        return new MoveUnitCommand(unit, destX, unit->y());
    }
    if (isPressed(ButtonType::BUTTON_LEFT)) {
        int destX = unit->x() - 1;
        return new MoveUnitCommand(unit, destX, unit->y());
    }

    return nullptr;
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