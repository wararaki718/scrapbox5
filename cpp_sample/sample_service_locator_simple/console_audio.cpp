#include <iostream>

#include "console_audio.hpp"


void ConsoleAudio::playSound(int soundID)
{
    std::cout << "console audio play sound: " << soundID << std::endl;
}


void ConsoleAudio::stopSound(int soundID)
{
    std::cout << "console audio stop sound: " << soundID << std::endl;
}


void ConsoleAudio::stopAllSounds()
{
    std::cout << "console audio stop all sounds" << std::endl;
}
