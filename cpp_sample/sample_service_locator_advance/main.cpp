#include <iostream>

#include "audio.hpp"
#include "console_audio.hpp"
#include "locator.hpp"
#include "logged_audio.hpp"

void enableAudioLogging()
{
    auto *service = new LoggedAudio(
        Locator::getAudio()
    );

    Locator::provide(service);

    std::cout << "enable logged" << std::endl;
}


int main()
{
    Locator::provide(new ConsoleAudio());
    enableAudioLogging();
    // auto audio = Locator::getAudio();
    // audio->playSound(1);
    // audio->stopSound(1);
    // audio->stopAllSounds();

    std::cout << "DONE" << std::endl;

    return 0;
}
