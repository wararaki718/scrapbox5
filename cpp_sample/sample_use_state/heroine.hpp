#ifndef HEROINE_HPP
#define HEROINE_HPP

#include "image.hpp"
#include "input.hpp"
#include "state.hpp"


class Heroine
{
    public:
    void handleInput(InputType);
    void update();

    private:
    void setGraphic(ImageType);
    void superBomb();

    State state_{State::STATE_STANDING};
    int yVelocity_{0};
    int chargeTime_{0};
};

#endif // HEROINE_HPP
