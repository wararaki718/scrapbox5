#include <iostream>

#include "sound.hpp"
#include "soundplayer.hpp"


void SoundPlayer::playSound(SoundId sound)
{
    switch (sound)
    {
    case BGM:
        std::cout << "play bgm" << std::endl;
        break;
    
    case SOUND_SPROING:
        std::cout << "play sproing" << std::endl;
        break;
    
    case SOUND_SWOOP:
        std::cout << "play swoop" << std::endl;
        break;
    
    case SOUND_DIVE:
        std::cout << "play dive" << std::endl;
        break;
    
    default:
        break;
    }
}

void SoundPlayer::stopSound(SoundId sound)
{
    switch (sound)
    {
    case BGM:
        std::cout << "stop bgm" << std::endl;
        break;
    
    case SOUND_SPROING:
        std::cout << "stop sproing" << std::endl;
        break;
    
    case SOUND_SWOOP:
        std::cout << "stop swoop" << std::endl;
        break;
    
    case SOUND_DIVE:
        std::cout << "stop dive" << std::endl;
        break;
    
    default:
        break;
    }
}

void SoundPlayer::setVolume(SoundId sound)
{
    switch (sound)
    {
    case BGM:
        std::cout << "set bgm" << std::endl;
        break;
    
    case SOUND_SPROING:
        std::cout << "set sproing" << std::endl;
        break;
    
    case SOUND_SWOOP:
        std::cout << "set swoop" << std::endl;
        break;
    
    case SOUND_DIVE:
        std::cout << "set dive" << std::endl;
        break;
    
    default:
        break;
    }
}