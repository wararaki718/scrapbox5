#ifndef DEMON_HPP
#define DEMON_HPP

#include "monster.hpp"


class Demon: public Monster {
    public:
    Demon(int health, int speed): health_(health), speed_(speed) {}
    virtual Monster* clone();
    virtual void show();

    private:
    int health_;
    int speed_;
};

#endif // DEMON_HPP
