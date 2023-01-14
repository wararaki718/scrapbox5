#include "spawner.hpp"


Monster* Spawner::spawnMonster()
{
    return prototype_->clone();
}
