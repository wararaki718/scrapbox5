#ifndef NULL_AUDIO_HPP
#define NULL_AUDIO_HPP

#include "audio.hpp"

class NullAudio: public Audio
{
    public:
    virtual void playSound(int soundID) {};
    virtual void stopSound(int soundID) {};
    virtual void stopAllSounds() {};
};

#endif // NULL_AUDIO_HPP
