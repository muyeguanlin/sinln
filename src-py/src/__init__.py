from .download import BaiduImageDownloader
from .database import DatabaseManager

# 在__init__.py中写入上面两句

# python
# # 简化前
# from mod.download import BaiduImageDownloader
# from mod.database import DatabaseManager

# # 简化后
# from mod import BaiduImageDownloader, DatabaseManager
# # 或者
# import mod
# downloader = mod.BaiduImageDownloader()
# 标识包目录：在 Python 中，一个目录只有包含 __init__.py 文件才会被视作一个包（package）。这样，Python 解释器才会将该目录当做包来处理，从而可以导入该目录下的模块。
# 允许使用点号导入：import mod.download 而不是文件路径导入


# Python 3.3+ 会自动识别为包

__all__ = ['BaiduImageDownloader', 'DatabaseManager']