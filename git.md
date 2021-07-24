# Git与Github

## fork别人仓库后如何保持同步
进入本地目录，执行：
```
$ git remote//如果只有origin没有upstream，继续执行以添加upstream，否则跳过下面2条命令
$ git remote -v | --verbose 
$ git remote add upstream https://github.com/xxxx/xxxxx(你fork的仓库的地址)
$ git add .
$ git commit -m 'note'
$ git push
$ git fetch upstream
$ git checkout main  //以前是master
$ git merge upstream/main
$ git push 
```