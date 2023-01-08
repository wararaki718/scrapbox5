#ifndef SUBJECT_HPP
#define SUBJECT_HPP

#include "entity.hpp"
#include "event.hpp"
#include "observer.hpp"
#include "params.hpp"


class Subject
{
    public:
    void addObserver(Observer* observer);
    void removeObserver(Observer* observer);
    void onNotify(Entity&, Event);

    private:
    Observer* observers_[MAX_OBSERVERS];
    int numObservers_{0};

    protected:
    void notify(Entity&, Event);
};


#endif // SUBJECT_HPP