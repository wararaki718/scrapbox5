#ifndef GRID_HPP
#define GRID_HPP

class Unit;

class Grid
{
    public:
    Grid()
    {
        for (int x = 0; x < NUM_CELLS; x++)
        {
            for (int y = 0; y < NUM_CELLS; y++)
            {
                cells_[x][y] = nullptr;
            }
        }
    }
    void add(Unit*);
    void handleMelee();
    void handleCell(int, int);
    void handleUnit(Unit*, Unit*);
    void handleAttack(Unit*, Unit*);
    void move(Unit*, double, double);
    double distance(Unit*, Unit*);

    static const int NUM_CELLS = 10;
    static const int CELL_SIZE = 20;
    double ATTACK_DISTANCE{5.0};

    private:
    Unit* cells_[NUM_CELLS][NUM_CELLS];
};

#endif // GRID_HPP
