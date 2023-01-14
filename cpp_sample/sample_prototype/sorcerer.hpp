#ifndef SORCERER_HPP
#define SORCERER_HPP

#include "monster.hpp"

class Sorcerer: public Monster {
    public:
    Sorcerer(int health, int speed): health_(health), speed_(speed) {}
    virtual Monster* clone();
    virtual void show();

    private:
    int health_;
    int speed_;
};

#endif // SORCERER_HPP
