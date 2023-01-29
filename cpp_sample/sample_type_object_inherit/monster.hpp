#ifndef MONSTER_HPP
#define MONSTER_HPP

class Breed;

class Monster
{
    friend class Breed;

    public:
    const char* getAttack();

    private:
    Monster(Breed& breed);
    int health_;
    Breed& breed_;
};

#endif // MONSTER_HPP
