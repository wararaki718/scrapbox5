#ifndef LOCATOR_HPP
#define LOCATOR_HPP

#include "audio.hpp"


class Locator
{
    public:
    static Audio* getAudio() { return service_; }
    static void provide(Audio* service) { service_ = service; }

    private:
    static Audio* service_;
};

Audio* Locator::service_ = nullptr;

#endif // LOCATOR_HPP
