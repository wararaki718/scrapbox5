#include <iostream>

#include "achievements.hpp"
#include "entity.hpp"
//#include "event.hpp"
#include "physics.hpp"
#include "subject.hpp"


int main()
{
    Achievements* achievements = new Achievements();
    Subject subject = Subject();
    subject.addObserver(achievements);
    subject.removeObserver(achievements);

    Entity entity = Entity(true);
    Physics physics = Physics();

    physics.updateEntity(entity);

    Event event = Event::EVENT_START_FALL;
    achievements->onNotify(entity, event);

    std::cout << "DONE" << std::endl;
    return 0;
}
