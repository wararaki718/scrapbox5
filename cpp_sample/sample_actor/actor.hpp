#ifndef ACTOR_HPP
#define ACTOR_HPP

#include <string>

class GameActor
{
    public:
    GameActor() {}
    GameActor(std::string name_) : name(name_) {}
    void jump();
    void fire();
    void lurch();
    void swap();

    private:
    std::string name {"default"};
};


#endif // ACTOR_HPP