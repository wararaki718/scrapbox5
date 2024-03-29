#ifndef SORCERER_HPP
#define SORCERER_HPP

#include "monster.hpp"

class Sorcerer: public Monster {
    public:
    Sorcerer() {}
    Sorcerer(int health, int speed): health_(health), speed_(speed) {}
    virtual void show();

    private:
    int health_{0};
    int speed_{0};
};

#endif // SORCERER_HPP
