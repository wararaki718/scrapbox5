#ifndef GHOST_HPP
#define GHOST_HPP

#include "monster.hpp"

class Ghost: public Monster {
    public:
    Ghost(int health, int speed): health_(health), speed_(speed) {}
    virtual Monster* clone();
    virtual void show();

    private:
    int health_;
    int speed_;
};

#endif // GHOST_HPP