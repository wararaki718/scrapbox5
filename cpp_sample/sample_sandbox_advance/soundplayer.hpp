#ifndef SOUNDPLAYER_HPP
#define SOUNDPLAYER_HPP

#include "sound.hpp"


class SoundPlayer
{
    public:
    void playSound(SoundId);
    void stopSound(SoundId);
    void setVolume(SoundId);
};

#endif // SOUNDPLAYER_HPP
