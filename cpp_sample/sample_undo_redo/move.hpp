#ifndef MOVE_HPP
#define MOVE_HPP

#include "command.hpp"
#include "unit.hpp"

class MoveUnitCommand : public Command
{
    public:
    MoveUnitCommand(Unit* unit, int x, int y) : unit_(unit), x_(x), y_(y), xBefore_(0), yBefore_(0) {}
    void execute();
    void undo();

    private:
    Unit* unit_;
    int x_;
    int y_;
    int xBefore_;
    int yBefore_;
};

#endif // MOVE_HPP
