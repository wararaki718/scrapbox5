#ifndef ACHIEVEMENTS_HPP
#define ACHIEVEMENTS_HPP

#include "achievement.hpp"
#include "entity.hpp"
#include "event.hpp"
#include "observer.hpp"


class Achievements : public Observer
{
    public:
    void onNotify(Entity&, Event);

    private:
    void unlock(Achievement);
    bool heroIsOnBridge_{true};
};

#endif // ACHIEVENTS_HPP
