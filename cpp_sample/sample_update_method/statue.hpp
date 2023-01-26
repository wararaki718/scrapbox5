#ifndef STATUE_HPP
#define STATUE_HPP

#include "entity.hpp"


class Statue: public Entity
{
public:
    Statue() {}
    Statue(int delay): delay_(delay) {}

    virtual void update();

private:
    int frames_{0};
    int delay_{0};

    void shootLightning();
};

#endif // STATUE_HPP
