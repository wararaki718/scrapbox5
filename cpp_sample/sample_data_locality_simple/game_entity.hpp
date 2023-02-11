#ifndef GAME_ENTITY_HPP
#define GAME_ENTITY_HPP

#include "ai_component.hpp"
#include "physics_component.hpp"
#include "render_component.hpp"


class GameEntity
{
    public:
    GameEntity(
        AIComponent* ai,
        PhysicsComponent* physics,
        RenderComponent* render
    ): ai_(ai), physics_(physics), render_(render) {}

    AIComponent* ai();
    PhysicsComponent* physics();
    RenderComponent* render();

    private:
    AIComponent* ai_;
    PhysicsComponent* physics_;
    RenderComponent* render_;
};

#endif // GAME_ENTITY_HPP
