#include <iostream>

#include "audio.hpp"
#include "console_audio.hpp"
#include "locator.hpp"


int main()
{
    Locator::provide(new ConsoleAudio());
    auto audio = Locator::getAudio();
    audio->playSound(1);
    audio->stopSound(1);
    audio->stopAllSounds();

    std::cout << "DONE" << std::endl;

    return 0;
}
