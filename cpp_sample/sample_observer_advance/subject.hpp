#ifndef SUBJECT_HPP
#define SUBJECT_HPP

#include "entity.hpp"
#include "event.hpp"
#include "observer.hpp"

class Subject
{
    public:
    Subject(): head_(nullptr) {}

    void addObserver(Observer*);
    void removeObserver(Observer*);
    void notify(Entity&, Event);

    private:
    Observer* head_;
};

#endif // SUBJECT_HPP
