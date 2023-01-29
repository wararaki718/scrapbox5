#include "breed.hpp"
#include "monster.hpp"


Monster::Monster(Breed& breed): health_(breed.getHealth()), breed_(breed) {}


const char* Monster::getAttack()
{
    return breed_.getAttack();
}
