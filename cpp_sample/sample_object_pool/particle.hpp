#ifndef PARTICLE_HPP
#define PARTICLE_HPP

class Particle
{
    public:
    Particle() {}

    void init(double, double, double, double, int);
    bool animate();

    bool inUse() const;

    Particle* getNext() const;
    void setNext(Particle*);

    private:
    int framesLeft_{0};

    union
    {
        struct {
            double x_;
            double y_;
            double xVel_;
            double yVel_;
        } live;
        Particle* next;
    } state_;
};

#endif // PARTICLE_HPP
