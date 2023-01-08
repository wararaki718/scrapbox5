#include <iostream>

#include "subject.hpp"


void Subject::addObserver(Observer* observer)
{
    std::cout << "add" << std::endl;
    observers_[numObservers_] = observer;
    numObservers_++;
}


void Subject::removeObserver(Observer* observer)
{
    std::cout << "remove" << std::endl;
    numObservers_--;
}


void Subject::notify(Entity& entity, Event event)
{
    for(int i = 0; i < numObservers_; i++) {
        observers_[i]->onNotify(entity, event);
    }
}

void Subject::onNotify(Entity& entity, Event event)
{
    std::cout << "on notify" << std::endl;
}
