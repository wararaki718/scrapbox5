#ifndef PARTICLE_HPP
#define PARTICLE_HPP

class Particle
{
    public:
    Particle() {}

    void init(double, double, double, double, int);
    void animate();

    bool inUse() const;

    private:
    int framesLeft_{0};
    double x_;
    double y_;
    double xVel_;
    double yVel_;
};

#endif // PARTICLE_HPP
