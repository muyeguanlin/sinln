import sys
import os
import modules

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 构建 `build/debug` 的相对路径（假设脚本在项目根目录）
build_debug_dir = os.path.join(script_dir, "build", "debug")

# 添加到 Python 模块搜索路径
sys.path.append(build_debug_dir)

import example # type: ignore
from example import MathUtils, StringUtils# type: ignore #引入类

print(example.add(2, 3))      # 输出: 5
print(example.greet("Alice")) # 输出: Hello, Alice!

print(example.MathUtils.square(4))       # 输出: 16
print(example.StringUtils.reverse("abc")) # 输出: cba

print(example.math.add(2, 3))          # 输出: 5
print(example.str.uppercase("hello"))  # 输出: HELLO
print("就行了，脸说爱的故") # 输出: HELLO




print(modules.sum_as_string(5, 10))  # 输出 "15"
