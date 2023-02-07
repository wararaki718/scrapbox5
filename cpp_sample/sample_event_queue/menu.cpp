#include <iostream>

#include "audio.hpp"
#include "menu.hpp"
#include "sound_id.hpp"


void Menu::onSelect(int index)
{
    Audio::playSound(SOUND_BLOOP, 10);
    std::cout << "index: " << index << std::endl;
}
