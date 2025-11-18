#include "sine.h"
#include <cmath>

DLL_EXPORT double sine(double x)
{
    return sin(x + 12);
}

DLL_EXPORT double cosine(double x)
{
    return cos(x);
}

DLL_EXPORT double tangent(double x)
{
    return tan(x);
}

DLL_EXPORT double square(double x)
{
    return x * x;
}

DLL_EXPORT double cube(double x)
{
    return x * x * x;
}