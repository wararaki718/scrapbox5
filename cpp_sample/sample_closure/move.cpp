#include <functional>
#include <iostream>
#include <map>
#include <string>
#include "unit.hpp"
#include "move.hpp"


std::map<std::string, std::function<void(void)>> makeMoveUnitCommand(Unit* unit, int x, int y) {
    int xBefore = unit->x(), yBefore = unit->y();
    std::cout << "call x: " << x << ",y: " << y << std::endl;
    std::cout << "call x: " << unit->x() << ",y: " << unit->y() << std::endl;
    
    auto execute = [&](){
        xBefore = unit->x();
        yBefore = unit->y();
        unit->moveTo(x, y);
        std::cout << "move x: " << unit->x() << ",y: " << unit->y() << std::endl;
    };
    auto undo = [&](){
        unit->moveTo(xBefore, yBefore);
        std::cout << "undo" << std::endl;
    };

    std::map<std::string, std::function<void(void)>> commands;
    commands.insert(std::make_pair("execute", execute));
    commands.insert(std::make_pair("undo", undo));
    return commands;
}
