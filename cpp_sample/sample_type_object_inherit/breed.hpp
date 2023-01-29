#ifndef BREED_HPP
#define BREED_HPP

class Monster;

class Breed
{
    public:
    Breed() {}
    Breed(Breed* parent, int health, const char* attack);

    int getHealth();
    const char* getAttack();
    Monster* newMonster();

    private:
    Breed* parent_;
    int health_;
    const char* attack_;
};

#endif // BREED_HPP
