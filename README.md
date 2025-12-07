## 上传到 github

git config --global user.name "muyeguanlin"
git config --global user.email "2390893447@qq.com"
git init

git status
git add .

# 3. 提交更改

git commit -m "feat: mysql 语句一"

类型 说明 示例
feat 新功能 feat: 添加用户注册功能
fix 修复 bug fix: 修复登录页面的崩溃问题  
docs 文档更新 docs: 更新 API 接口文档
style 代码格式调整 style: 调整代码缩进
refactor 重构代码 refactor: 重构用户验证逻辑
test 测试相关 test: 添加登录功能单元测试
chore 构建过程或辅助工具变动 chore: 更新 webpack 配置

        # 1. 删除现有冲突的远程仓库

        git remote remove origin

        # 2. 添加 Gitee 为主要远程仓库（访问速度快）

        git remote add origin https://gitee.com/muyeguanlin/sinln.git

        # 3. 可选：添加 GitHub 作为次要远程

        git remote add github https://github.com/muyeguanlin/sinln.git

# 4. 拉取远程最新代码（避免冲突）

# 在推送之前，先拉取远程仓库的最新更改，并合并到你的当前分支：

git pull origin main

# 4. 推送到 Gitee

git push -u origin main

# 5. 如果需要，再推送到 GitHub

git push -u github main

# 同样，如果你使用的是其他分支，请替换 main 为你的分支名。

# 如果你之前已经设置过上游分支，可以直接使用：

git push

# 我们已经在项目根目录建立了本地仓库，因为用户已经执行了 git init，并且看到了提示：Initialized empty Git repository in F:/study251011/sinln/.git/

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
