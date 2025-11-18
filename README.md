## 上传到 github

git config --global user.name "muyeguanlin"
git config --global user.email "2390893447@qq.com"
git init
git status
git add .
Remove-Item -Recurse -Force sinln\.git
git commit -m "origin"
git remote add origin https://github.com/muyeguanlin/sinln.git
git remote add origin https://gitee.com/qq2390893447/myproject.git
git commit -m "修复 Git 子仓库问题，添加所有项目文件"
git push -u origin main

我们已经在项目根目录建立了本地仓库，因为用户已经执行了 git init，并且看到了提示：Initialized empty Git repository in F:/study251011/sinln/.git/

## 检查上传文件

git status
Remove-Item -Recurse -Force sinln\.git## 清除缓存

## tauri

更换 icon cargo tauri icon new-icon.png
Prevents additional console window on Windows in release, DO NOT REMOVE!!
