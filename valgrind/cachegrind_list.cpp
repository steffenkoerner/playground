#include <iostream>
#include <list>
#include <numeric>
#include <chrono>


int main() {
    using std::chrono::high_resolution_clock;
    using std::chrono::duration_cast;
    using std::chrono::duration;
    using std::chrono::milliseconds;

    std::list<long> v( 100'000'000, 1);

    auto t1 = high_resolution_clock::now();
    int i = 0;
    for(const auto& element : v) {
        ++i;
    }
    auto t2 = high_resolution_clock::now();

    duration<double, std::milli> ms_double = t2 - t1;
    std::cout << ms_double.count() << "ms\n";

    return 0;
}