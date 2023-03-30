#include <iostream>
#include <chrono>
#include <thread>

void LeakingMemory() {
    std::this_thread::sleep_for(std::chrono::milliseconds(10000));
}

void DoSomething() {
    LeakingMemory();
    std::this_thread::sleep_for(std::chrono::milliseconds(30000));
}

int main() {
    std::cout << "I am running" << std::endl;
    DoSomething();
    return 0;
}