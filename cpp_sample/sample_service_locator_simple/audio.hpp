#ifndef AUDIO_HPP
#define AUDIO_HPP

class Audio
{
    public:
    virtual ~Audio() {}
    virtual void playSound(int soundID) = 0;
    virtual void stopSound(int soundID) = 0;
    virtual void stopAllSounds() = 0;
};

#endif // AUDIO_HPP
