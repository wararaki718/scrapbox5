#ifndef VM_HPP
#define VM_HPP

class VM
{
    public:
    void interpret(char [], int);

    private:
    static const int MAX_STACK = 128;
    int stackSize_{0};
    int stack_[MAX_STACK];

    void push(int);
    int pop();
};

#endif // VM_HPP
