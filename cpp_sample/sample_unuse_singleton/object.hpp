#ifndef OBJECT_HPP
#define OBJECT_HPP

#include "log.hpp"

class GameObject
{
    public:
    GameObject() {
        log_ = Log();
    }
    //protected:
    //Log& log();

    public:
    static Log& log_;
};

#endif // OBJECT_HPP
