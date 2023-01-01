#ifndef MOVE_HPP
#define MOVE_HPP

#include <functional>
#include <map>
#include <string>
#include "unit.hpp"

std::map<std::string, std::function<void(void)>> makeMoveUnitCommand(Unit*, int, int);

#endif // MOVE_HPP