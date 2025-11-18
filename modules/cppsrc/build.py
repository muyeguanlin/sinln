# import os
# import subprocess
# import sys
# from pathlib import Path

# # 配置
# build_dir = Path("build")
# src_dir = Path("src")
# include_dir = Path("include")

# # 确保目录存在
# build_dir.mkdir(exist_ok=True)

# # 使用绝对路径更可靠
# cl_exe = r"G:\vs2022\Professional\VC\Tools\MSVC\14.42.34433\bin\Hostx64\x64\cl.exe"
# include_path = include_dir.resolve()  # 获取绝对路径

# compile_cmd = [
#     cl_exe,
#     "/nologo",
#     "/Zi",
#     "/W4",
#     "/O2",
#     "/EHsc",
#     f"/I{include_path}",  # 使用绝对路径
#     "/DSINE_EXPORTS",
#     "/MD",
#     "/c",
#     "src/sine.cpp",
#     f"/Fo{build_dir}/sine.obj"
# ]

# print("执行编译命令:", " ".join(compile_cmd))
# result = subprocess.run(compile_cmd)
# if result.returncode != 0:
#     print("编译失败")
#     sys.exit(1)

# # 链接命令
# link_exe = cl_exe.replace("cl.exe", "link.exe")
# link_cmd = [
#     link_exe,
#     "/nologo",
#     "/DLL",
#     "/DEBUG",
#     f"{build_dir}/sine.obj",
#     f"/OUT:{build_dir}/sine.dll"
# ]

# print("执行链接命令:", " ".join(link_cmd))
# result = subprocess.run(link_cmd)
# if result.returncode == 0:
#     print(f"成功构建 {build_dir}/sine.dll")
# else:
#     print("链接失败")
#     sys.exit(1)

######################################################################
# ###异步无ninja
# import asyncio
# import os
# import sys
# from pathlib import Path

# async def run_command(cmd, cwd=None):
#     """异步执行命令并处理编码问题"""
#     process = await asyncio.create_subprocess_exec(
#         *cmd,
#         cwd=cwd,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE
#     )
    
#     async def print_stream(stream, prefix):
#         while True:
#             line = await stream.readline()
#             if not line:
#                 break
#             try:
#                 print(f"{prefix}: {line.decode('utf-8').strip()}")
#             except UnicodeDecodeError:
#                 print(f"{prefix}: [编码转换] {line.decode('gbk', errors='replace').strip()}")
    
#     await asyncio.gather(
#         print_stream(process.stdout, "OUT"),
#         print_stream(process.stderr, "ERR")
#     )
    
#     return await process.wait()

# async def compile_sine():
#     """异步编译流程"""
#     # 获取项目根目录
#     project_root = Path(__file__).parent
#     build_dir = project_root / "build"
#     src_dir = project_root / "src"
#     include_dir = project_root / "include"
    
#     # 确保构建目录存在
#     build_dir.mkdir(exist_ok=True)
    
#     # MSVC 工具路径
#     vc_path = Path(r"G:\vs2022\Professional\VC\Tools\MSVC\14.42.34433\bin\Hostx64\x64")
#     cl_exe = vc_path / "cl.exe"
#     link_exe = vc_path / "link.exe"
    
#     # 检查工具是否存在
#     if not cl_exe.exists():
#         raise FileNotFoundError(f"编译器未找到: {cl_exe}")
#     if not link_exe.exists():
#         raise FileNotFoundError(f"链接器未找到: {link_exe}")
    
#     # 编译命令
#     compile_cmd = [
#         str(cl_exe),
#         "/nologo",
#         "/Zi",
#         "/W4",
#         "/O2",
#         "/EHsc",
#         f"/I{str(include_dir)}",
#         "/DBUILD_DLL",  # <<< 但在编译时 BUILD_DLL 宏没有被定义 导致编译器误将函数视为 dllimport 而非 dllexport
#         "/DSINE_EXPORTS",
#         "/MD",
#         "/c",
#         str(src_dir / "sine.cpp"),
#         f"/Fo{str(build_dir / 'sine.obj')}"
#     ]
    
#     print("🛠 开始异步编译...")
#     print("执行命令:", " ".join(compile_cmd))
#     compile_ret = await run_command(compile_cmd, cwd=project_root)
#     if compile_ret != 0:
#         raise RuntimeError(f"编译失败，退出码: {compile_ret}")
    
#     # 链接命令
#     link_cmd = [
#         str(link_exe),
#         "/nologo",
#         "/DLL",
#         "/DEBUG",
#         str(build_dir / "sine.obj"),
#         f"/OUT:{str(build_dir / 'sine.dll')}"
#     ]
    
#     print("🔗 开始异步链接...")
#     print("执行命令:", " ".join(link_cmd))
#     link_ret = await run_command(link_cmd, cwd=project_root)
#     if link_ret != 0:
#         raise RuntimeError(f"链接失败，退出码: {link_ret}")
    
#     print(f"✅ 成功构建 {build_dir/'sine.dll'}")

# async def main():
#     try:
#         await compile_sine()
#     except Exception as e:
#         print(f"❌ 构建出错: {str(e)}", file=sys.stderr)
#         return 1
#     return 0

# if __name__ == "__main__":
#     # Windows 特定设置
#     if os.name == 'nt':
#         asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        
#         # 确保加载了 MSVC 环境变量
#         vcvars = Path(r"G:\vs2022\Professional\VC\Auxiliary\Build\vcvars64.bat")
#         if vcvars.exists():
#             os.system(f'call "{vcvars}"')
    
#     # 设置控制台编码
#     if sys.stdout.encoding != 'utf-8':
#         import io
#         sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
#         sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
#     exit_code = asyncio.run(main())
#     sys.exit(exit_code)

###################################################################################################
import os
import subprocess
from pathlib import Path
# import test

# def generate_build_ninja():
#     # GCC编译器配置
#     cxx = "g++"
#     cflags = "-O2 -Wall -Wextra -fPIC -I. -DSINE_EXPORTS -D_WINDLL -D_USE_MATH_DEFINES"
#     ldflags = "-shared"
    
#     # 源文件和目标文件
#     sources = ["sine.cpp", "sine_interface.cpp"]
#     objects = [f"{Path(src).stem}.o" for src in sources]
    
#     # 输出目录
#     build_dir = "build"
#     os.makedirs(build_dir, exist_ok=True)
    
#     # 生成 build.ninja 内容
#     ninja_content = f"""
# # 变量定义
# cxx = {cxx}
# cflags = {cflags}
# ldflags = {ldflags}

# # 构建规则
# rule compile
#   command = $cxx $cflags -c $in -o $out
#   description = 编译 $in -> $out

# rule link
#   command = $cxx $ldflags $in -o $out
#   description = 链接 $out

# # 构建目标
# """

#     # 添加对象文件构建规则
#     for src, obj in zip(sources, objects):#result = dict(zip(sources, objects))    print(result) zip(*pairs) 
#         ninja_content += f"build {build_dir}/{obj}: compile {src}\n"

#     # 添加 DLL 构建规则
#     output_name = "sine.dll" if os.name == 'nt' else "libsine.so"
#     ninja_content += f"""
# build {build_dir}/{output_name}: link {' '.join(f'{build_dir}/{obj}' for obj in objects)}
# """

#     # 写入 build.ninja 文件
#     with open("build.ninja", "w", encoding="utf-8") as f:
#         f.write(ninja_content)

# def create_source_files():
#     # 创建 UTF-8 编码的源文件
#     sine_h_content = """// sine.h - 正弦函数接口头文件
# #ifndef SINE_H
# #define SINE_H

# #ifdef _WIN32
#     #ifdef SINE_EXPORTS
#         #define SINE_API __declspec(dllexport)
#     #else
#         #define SINE_API __declspec(dllimport)
#     #endif
# #else
#     #define SINE_API __attribute__((visibility("default")))
# #endif

# #include <cmath>

# extern "C" SINE_API double calculate_sine(double x);
# extern "C" SINE_API void generate_sine_wave(double* output, int length, double amplitude, double frequency, double phase);
# extern "C" SINE_API void process_sine_array(double* input, double* output, int length, double factor);

# #endif // SINE_H
# """
#     with open("sine.h", "w", encoding="utf-8") as f:
#         f.write(sine_h_content)

#     sine_cpp_content = """// sine.cpp - 正弦函数实现
# #include "sine.h"
# #define SINE_EXPORTS

# double calculate_sine(double x) { return std::sin(x); }

# void generate_sine_wave(double* output, int length, double amplitude, double frequency, double phase) {
#     const double pi = 3.14159265358979323846;
#     for (int i = 0; i < length; ++i) {
#         output[i] = amplitude * std::sin(2.0 * pi * frequency * i / length + phase);
#     }
# }

# void process_sine_array(double* input, double* output, int length, double factor) {
#     for (int i = 0; i < length; ++i) {
#         output[i] = factor * std::sin(input[i]);
#     }
# }
# """
#     with open("sine.cpp", "w", encoding="utf-8") as f:
#         f.write(sine_cpp_content)

#     sine_interface_cpp_content = """// sine_interface.cpp - 附加接口实现
# #include "sine.h"

# extern "C" SINE_API double sine_of_sum(double a, double b) {
#     return calculate_sine(a + b);
# }
# """
#     with open("sine_interface.cpp", "w", encoding="utf-8") as f:
#         f.write(sine_interface_cpp_content)

def check_gcc_available():
    try:
        subprocess.run(["g++", "--version"], check=True, capture_output=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def build_project():
    if not check_gcc_available():
        print("错误: 未找到 g++ 编译器。请安装 MinGW-w64 并确保在 PATH 中")
        print("Windows 用户可以从 https://www.mingw-w64.org/ 下载安装")
        return
    
    try:
        subprocess.run(["ninja", "--version"], check=True, capture_output=True)
    except FileNotFoundError:
        print("错误: 未找到 ninja 构建工具")
        return
    
    try:
        subprocess.run(["ninja"], check=True)
        print("\n构建成功！输出文件: build/sine.dll" if os.name == 'nt' else "build/libsine.so")
    except subprocess.CalledProcessError as e:
        print(f"\n构建失败了: {e}")

if __name__ == "__main__":
    # print("正在创建源文件...")
    # create_source_files()
    
    # print("正在生成 build.ninja...")
    # generate_build_ninja()
    
  

    print("开始构建项目fsf...")
    build_project()

    # test.run()