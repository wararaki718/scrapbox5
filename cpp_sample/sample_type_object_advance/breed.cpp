#include "breed.hpp"
#include "monster.hpp"


Breed::Breed(int health, const char* attack): health_(health), attack_(attack) {}


int Breed::getHealth()
{
    return health_;
}

const char* Breed::getAttack()
{
    return attack_;
}

Monster* Breed::newMonster() {
    return new Monster(*this);
}
