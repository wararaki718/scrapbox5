#include <iostream>

#include "achievement.hpp"
#include "achievements.hpp"
#include "entity.hpp"
#include "event.hpp"


void Achievements::onNotify(Entity& entity, Event event)
{
    std::cout << "achievement onNotify" << std::endl;
    switch(event) {
        case Event::EVENT_START_FALL:
            std::cout << entity.isHero() << " " << heroIsOnBridge_ << std::endl;
            if(entity.isHero() && heroIsOnBridge_) {
                unlock(Achievement::ACHIEVEMENT_FELL_OFF_BRIDGE);
            }
            break;
    }
}


void Achievements::unlock(Achievement achievement)
{
    switch (achievement)
    {
        case Achievement::ACHIEVEMENT_FELL_OFF_BRIDGE:
            std::cout << "fell off bridge" << std::endl;
            break;
        default:
            break;
    }
}
