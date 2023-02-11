#include <iostream>

#include "ai_component.hpp"
#include "physics_component.hpp"
#include "render_component.hpp"

#define MAX_ENTITIES 10


int main()
{
    int k = 0;
    int numEntities = 1;
    auto aiComponents = new AIComponent[MAX_ENTITIES];
    auto physicsComponents = new PhysicsComponent[MAX_ENTITIES];
    auto renderComponents = new RenderComponent[MAX_ENTITIES];

    for (int i = 0; i < numEntities; i++)
    {
        aiComponents[i] = AIComponent();
        physicsComponents[i] = PhysicsComponent();
        renderComponents[i] = RenderComponent();
    }

    while(k < 1)
    {
        for (int i = 0; i < numEntities; i++)
        {
            aiComponents[i].update();
        }

        for (int i = 0; i < numEntities; i++)
        {
            physicsComponents[i].update();
        }

        for (int i = 0; i < numEntities; i++)
        {
            renderComponents[i].update();
        }
        k++;
    }

    std::cout << "DONE" << std::endl;
    return 0;
}
