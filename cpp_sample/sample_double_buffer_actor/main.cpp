#include <iostream>

#include "comedian.hpp"
#include "stage.hpp"


int main()
{
    Stage stage;
    auto harry = new Comedian();
    auto baldy = new Comedian();
    auto chump = new Comedian();

    harry->face(baldy);
    baldy->face(chump);
    chump->face(harry);

    stage.add(harry, 0);
    stage.add(baldy, 1);
    stage.add(chump, 2);

    harry->slap();
    stage.update();

    std::cout << "DONE" << std::endl;
    return 0;
}