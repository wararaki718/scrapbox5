#ifndef SKELETON_HPP
#define SKELETON_HPP

#include "entity.hpp"


class Skeleton: public Entity
{
public:
    Skeleton() {}
    ~Skeleton() {}
    virtual void update();
private:
    bool patrollingLeft_{false};
};

#endif // SKELETON_HPP
