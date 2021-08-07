import os

# if dont have Initialized empty Git repository in project/git-submodule-demo/.git/
os.system('git checkout <branch-name> && git submodule add -b <branch-name> <git@provider-submodule.com>:<username/repository.git> <path> && git add .gitmodules <submodule-name/> &&  git commit -a git push -u <remote> <branch>">')
