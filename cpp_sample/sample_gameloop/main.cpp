#include <iostream>
#include <chrono>

#define MS_PER_UPDATE 5

void processInput()
{
    std::cout << "process input" << std::endl;
}

void update()
{
    std::cout << "update" << std::endl;
}

void render()
{
    std::cout << "render" << std::endl;
    std::cout << "-----" << std::endl;
}

int main()
{
    int th = 10;
    int i = 0;

    auto previous = std::chrono::system_clock::now();
    double lag = 0.0;
    while(i < th)
    {
        auto current = std::chrono::system_clock::now();
        auto elapsed = (double)((current - previous).count());
        previous = current;
        lag += elapsed;

        processInput();

        while(lag >= MS_PER_UPDATE) {
            update();
            lag -= MS_PER_UPDATE;
        }
        render();
        i++;
    }
    return 0;
}
