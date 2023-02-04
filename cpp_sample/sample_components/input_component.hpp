#ifndef INPUT_COMPONENT_HPP
#define INPUT_COMPONENT_HPP

class Bjorn;

class InputComponent
{
    public:
    void update(Bjorn& bjorn);

    private:
    static const int WALK_ACCELERATION = 1;
};

#endif // INPUT_COMPONENT_HPP
