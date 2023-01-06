#ifndef POSITION_HPP
#define POSITION_HPP

class Position
{
    public:
    Position() {}
    Position(int x_, int y_, int z_): x(x_), y(y_), z(z_) {}

    int x{0};
    int y{0};
    int z{0};
};

#endif // POSITION_HPP