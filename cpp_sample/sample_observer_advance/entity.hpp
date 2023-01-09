#ifndef ENTITY_HPP
#define ENTITY_HPP


class Entity
{
    public:
    Entity() {}
    Entity(bool hero_): hero(hero_) {}

    bool isHero();
    bool isOnSurface();
    void update();

    private:
    bool surface{true};
    bool hero{false};
};

#endif // ENTITY_HPP
