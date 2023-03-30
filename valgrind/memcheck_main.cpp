#include <iostream>


void LeakingMemory() {
    int *copy = (int*)malloc(5 * sizeof(int));
}

void DoSomething() {
    LeakingMemory();
}

int main() {
    std::cout << "I am running" << std::endl;
    DoSomething();
    return 0;
}