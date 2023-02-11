#include "ai_component.hpp"
#include "game_entity.hpp"
#include "physics_component.hpp"
#include "render_component.hpp"


AIComponent* GameEntity::ai()
{
    return ai_;
}

PhysicsComponent* GameEntity::physics()
{
    return physics_;
}

RenderComponent* GameEntity::render()
{
    return render_;
}
