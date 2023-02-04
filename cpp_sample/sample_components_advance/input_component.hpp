#ifndef INPUT_COMPONENT_HPP
#define INPUT_COMPONENT_HPP

class GameObject;

class InputComponent
{
    public:
    virtual ~InputComponent() {}
    virtual void update(GameObject&) = 0;
};

#endif // INPUT_COMPONENT_HPP
