#ifndef OBSERVER_HPP
#define OBSERVER_HPP

#include "entity.hpp"
#include "event.hpp"
//#include "subject.hpp"

class Subject;

class Observer
{
    friend class Subject;
    public:
    Observer(): next_(nullptr) {}
    void onNotify(Entity&, Event);

    private:
    Observer* next_;
};

#endif // OBSERVER_HPP
