#ifndef MONSTER_HPP
#define MONSTER_HPP

class Monster
{
    public:
    virtual ~Monster() {}
    virtual Monster* clone() = 0;
    virtual void show() = 0;
};

#endif // MONSTER_HPP
