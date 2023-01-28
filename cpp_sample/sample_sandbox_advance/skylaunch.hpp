#ifndef SKYLAUNCH_HPP
#define SKYLAUNCH_HPP

#include "soundplayer.hpp"
#include "superpower.hpp"

class SkyLaunch : public Superpower
{
    public:
    SkyLaunch() : Superpower() {}
    void update();
    protected:
    virtual void activate();
};

#endif // SKYLAUNCH_HPP
