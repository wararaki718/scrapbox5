#include <iostream>

#include "entity.hpp"
#include "event.hpp"
#include "observer.hpp"
#include "subject.hpp"


int main()
{
    auto observer1 = new Observer();
    auto observer2 = new Observer();

    std::cout << "# add observer for subject" << std::endl;
    auto subject = Subject();
    subject.addObserver(observer1);
    subject.addObserver(observer2);

    std::cout << "# notify" << std::endl;
    auto entity = Entity();
    auto event = Event::EVENT_START_FALL;
    subject.notify(entity, event);
    
    std::cout << "# remove observer" << std::endl;
    subject.removeObserver(observer1);

    std::cout << "# notify" << std::endl;
    subject.notify(entity, event);

    std::cout << "DONE" << std::endl;
    return 0;
}
