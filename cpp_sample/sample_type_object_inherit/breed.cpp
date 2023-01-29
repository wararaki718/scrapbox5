#include "breed.hpp"
#include "monster.hpp"


Breed::Breed(Breed* parent, int health, const char* attack): parent_(parent), health_(health), attack_(attack)
{
    if (parent != nullptr) {
        if (health == 0) {
            health_ = parent->getHealth();
        }

        if (attack == nullptr) {
            attack_ = parent->getAttack();
        }
    }
}

int Breed::getHealth()
{
    if (health_ != 0 || parent_ == nullptr) {
        return health_;
    }
    return parent_->getHealth();
}

const char* Breed::getAttack()
{
    if (attack_ != nullptr || parent_ == nullptr) {
        return attack_;
    }
    return parent_->getAttack();
}

Monster* Breed::newMonster() {
    return new Monster(*this);
}
