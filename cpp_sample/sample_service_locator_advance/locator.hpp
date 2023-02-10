#ifndef LOCATOR_HPP
#define LOCATOR_HPP

#include "audio.hpp"
#include "null_audio.hpp"


class Locator
{
    public:
    static void initialize() { service_ = &nullService_; }
    static Audio& getAudio() { return *service_; }
    static void provide(Audio* service) {
        if (service == nullptr) {
            service = &nullService_;
        }
        service_ = service;
    }

    private:
    static Audio* service_;
    static NullAudio nullService_;
};

Audio* Locator::service_ = nullptr;
NullAudio Locator::nullService_ = NullAudio();

#endif // LOCATOR_HPP
