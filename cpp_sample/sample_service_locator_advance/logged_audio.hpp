#ifndef LOGGED_AUDIO_HPP
#define LOGGED_AUDIO_HPP

#include "audio.hpp"


class LoggedAudio: public Audio
{
    public:
    LoggedAudio(Audio &wrapped): wrapped_(wrapped) {}

    virtual void playSound(int soundID);
    virtual void stopSound(int soundID);
    virtual void stopAllSounds();

    private:
    void log(const char*);

    Audio &wrapped_;
};

#endif // LOGGED_AUDIO_HPP
