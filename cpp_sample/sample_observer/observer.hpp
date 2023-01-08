#ifndef OBSERVER_HPP
#define OBSERVER_HPP

#include "entity.hpp"
#include "event.hpp"

class Observer
{
    public:
    virtual ~Observer() {}
    virtual void onNotify(Entity&, Event) = 0;
};

#endif //OBSERVER_HPP
