#include <iostream>


int main()
{
    auto f = [](int a, int b) {return a + b;};
    int x = 1, y = 2;
    std::cout << f(x, y) << std::endl;
    return 0;
}
