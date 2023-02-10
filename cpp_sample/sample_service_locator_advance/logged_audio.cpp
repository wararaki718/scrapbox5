#include <iostream>

#include "logged_audio.hpp"


void LoggedAudio::playSound(int soundID)
{
    log("play sound");
    wrapped_.playSound(soundID);
}


void LoggedAudio::stopSound(int soundID)
{
    log("stop sound");
    wrapped_.stopSound(soundID);
}


void LoggedAudio::stopAllSounds()
{
    log("stop all sound");
    wrapped_.stopAllSounds();
}


void LoggedAudio::log(const char* message)
{
    std::cout << message << std::endl;
}
