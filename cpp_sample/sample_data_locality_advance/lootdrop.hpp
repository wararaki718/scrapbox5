#ifndef LOOTDROP_HPP
#define LOOTDROP_HPP

#include "loottype.hpp"

class AIComponent;

class LootDrop
{
    friend class AIComponent;
    LootType drop_;
    int minDrops_;
    int maxDrops_;
    double chanceOfDrop_;
};

#endif // LOOTDROP_HPP
