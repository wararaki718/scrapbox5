#ifndef TRANSFORM_HPP
#define TRANSFORM_HPP

class Transform
{
    public:
    static Transform origin()
    {
        return Transform();
    }

    Transform combine(Transform&);
};

#endif // TRANSFORM_HPP
