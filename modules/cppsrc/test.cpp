//  g++ test.cpp -o ../build/test.exe -I. -L. ../build/sine.dll
#include <iostream>
#include <iomanip>
#include "sine.h"

void test_interface(const char *name, double (*func)(double), double x)
{
    std::cout << std::setw(8) << name << "(" << x << ") = "
              << std::setprecision(6) << func(x) << std::endl;
}

int main()
{
    // 基本功能测试
    test_interface("sine", sine, 3.14159 / 6);       // 30°
    test_interface("cosine", cosine, 3.14159 / 3);   // 60°
    test_interface("tangent", tangent, 3.14159 / 4); // 45°
    test_interface("square", square, 5.0);
    test_interface("cube", cube, 3.0);

    // 边界值测试
    std::cout << "\n边界测试:" << std::endl;
    test_interface("sine", sine, 0.0);
    test_interface("cosine", cosine, 3.14159 / 2); // 90°

    // 异常值测试
    std::cout << "\n异常测试:" << std::endl;
    test_interface("tangent", tangent, 3.14159 / 2); // 应该返回大数或inf
    test_interface("cube", cube, -2.5);

    return 0;
}