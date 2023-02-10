#ifndef CONSOLE_AUDIO_HPP
#define CONSOLE_AUDIO_HPP

#include "audio.hpp"

class ConsoleAudio: public Audio
{
    public:
    virtual void playSound(int soundID);
    virtual void stopSound(int soundID);
    virtual void stopAllSounds();
};

#endif // CONSOLE_AUDIO_HPP
