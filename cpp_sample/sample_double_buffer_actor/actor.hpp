#ifndef ACTOR_HPP
#define ACTOR_HPP

class Actor
{
    public:
    Actor(): currentSlapped_(false) {}
    virtual ~Actor() {}
    virtual void update() = 0;
    void swap();
    void slap();
    bool wasSlapped();

    private:
    bool currentSlapped_;
    bool nextSlapped_;
};

#endif // ACTOR_HPP
