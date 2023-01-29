#ifndef BREED_HPP
#define BREED_HPP

class Breed
{
    public:
    Breed() {}
    Breed(int health, const char* attack): health_(health), attack_(attack) {}

    int getHealth();
    const char* getAttack();

    private:
    int health_;
    const char* attack_;
};

#endif // BREED_HPP
