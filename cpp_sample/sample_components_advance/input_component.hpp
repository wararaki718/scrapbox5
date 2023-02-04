#ifndef INPUT_COMPONENT_HPP
#define INPUT_COMPONENT_HPP

class Bjorn;

class InputComponent
{
    public:
    virtual ~InputComponent() {}
    virtual void update(Bjorn& bjron) = 0;
};

#endif // INPUT_COMPONENT_HPP
