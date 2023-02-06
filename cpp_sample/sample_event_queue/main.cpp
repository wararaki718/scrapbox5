#include <iostream>

#include "menu.hpp"

int main()
{
    auto menu = Menu();
    menu.onSelect(10);
    menu.onSelect(11);
    menu.onSelect(12);
    
    std::cout << "DONE" << std::endl;
    return 0;
}
