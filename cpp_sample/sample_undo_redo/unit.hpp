#ifndef UNIT_HPP
#define UNIT_HPP

class Unit {
    public:
    void moveTo(int, int);
    int y();
    int x();

    private:
    int x_{0};
    int y_{0};
};

#endif // UNIT_HPP