#include <helloWorldLibrary.h>

#include <iostream>

int main()
{

    Library lib;

    int b = lib.b;
    std::cout << "Hello World Executable is alive and b is: " << b << std::endl;
    std::cout << lib.addition(2, 40) << std::endl;
    return 0;
}
