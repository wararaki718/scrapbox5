#ifndef SKYLAUNCH_HPP
#define SKYLAUNCH_HPP

#include "superpower.hpp"

class SkyLaunch : public Superpower
{
    public:
    void update();
    protected:
    virtual void activate();
};

#endif // SKYLAUNCH_HPP
