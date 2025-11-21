## 上传到 github

git config --global user.name "muyeguanlin"
git config --global user.email "2390893447@qq.com"
git init
git status
git add .

# 1. 删除现有冲突的远程仓库

git remote remove origin

# 2. 添加 Gitee 为主要远程仓库（访问速度快）

git remote add origin https://gitee.com/muyeguanlin/sinln.git

# 3. 可选：添加 GitHub 作为次要远程

git remote add github https://github.com/muyeguanlin/sinln.git

# 4. 推送到 Gitee

git push -u origin main

# 5. 如果需要，再推送到 GitHub

git push -u github main

我们已经在项目根目录建立了本地仓库，因为用户已经执行了 git init，并且看到了提示：Initialized empty Git repository in F:/study251011/sinln/.git/
###############################
git config --global user.name "muyeguanlin"
git config --global user.email "16415617+muyeguanlin@user.noreply.gitee.com"

mkdir sinln
cd sinln
git init
touch README.md
git add README.md
git commit -m "first commit"
git remote add origin https://gitee.com/muyeguanlin/sinln.git
git push -u origin "master"

已有仓库?

cd existing_git_repo
git remote add origin https://gitee.com/muyeguanlin/sinln.git
git push -u origin "master"

## 检查上传文件

git status
Remove-Item -Recurse -Force sinln\.git## 清除缓存

## tauri

更换 icon cargo tauri icon new-icon.png
Prevents additional console window on Windows in release, DO NOT REMOVE!!
