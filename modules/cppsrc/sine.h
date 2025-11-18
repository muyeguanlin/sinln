#ifndef SINE_H
#define SINE_H

#ifdef _WIN32
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT __attribute__((visibility("default")))
#endif

extern "C"
{
    DLL_EXPORT double sine(double x);    // 正弦函数
    DLL_EXPORT double cosine(double x);  // 余弦函数
    DLL_EXPORT double tangent(double x); // 正切函数
    DLL_EXPORT double square(double x);  // 平方
    DLL_EXPORT double cube(double x);    // 立方
}

#endif