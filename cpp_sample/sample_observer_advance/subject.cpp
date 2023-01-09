#include "entity.hpp"
#include "event.hpp"
#include "subject.hpp"


void Subject::addObserver(Observer* observer)
{
    observer->next_ = head_;
    head_ = observer;
}


void Subject::removeObserver(Observer* observer)
{
    if (head_ == observer) {
        head_ = observer->next_;
        observer->next_ = nullptr;
        return;
    }

    Observer* current = head_;
    while(current != nullptr) {
        if (current->next_ == observer) {
            current->next_ = observer->next_;
            observer->next_ = nullptr;
            return;
        }

        current = current->next_;
    }
}


void Subject::notify(Entity& entity, Event event)
{
    Observer* observer = head_;
    while (observer != nullptr) {
        observer->onNotify(entity, event);
        observer = observer->next_;
    }
}
