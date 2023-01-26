#ifndef ENTITY_HPP
#define ENTITY_HPP

class Entity
{
public:
    Entity() {}
    virtual ~Entity() {}

    virtual void update() = 0;

    double x() const;
    double y() const;

    void setX(double);
    void setY(double);

private:
    double x_{0}, y_{0};
};

#endif // ENTITY_HPP
