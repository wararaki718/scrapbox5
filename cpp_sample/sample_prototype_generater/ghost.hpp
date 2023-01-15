#ifndef GHOST_HPP
#define GHOST_HPP

#include "monster.hpp"

class Ghost: public Monster {
    public:
    Ghost() {}
    Ghost(int health, int speed): health_(health), speed_(speed) {}
    virtual void show();

    private:
    int health_{0};
    int speed_{0};
};

#endif // GHOST_HPP