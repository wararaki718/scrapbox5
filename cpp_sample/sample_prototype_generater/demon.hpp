#ifndef DEMON_HPP
#define DEMON_HPP

#include "monster.hpp"


class Demon: public Monster {
    public:
    Demon() {}
    Demon(int health, int speed): health_(health), speed_(speed) {}
    virtual void show();

    private:
    int health_{0};
    int speed_{0};
};

#endif // DEMON_HPP
