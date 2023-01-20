#ifndef ENEMY_HPP
#define ENEMY_HPP

#include "log.hpp"
#include "object.hpp"


class Enemy: public GameObject
{
    public:
    Enemy() {
        log_ = Log();
    }
    void doSomething();
};

#endif // ENEMY_HPP