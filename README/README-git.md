# Basic of GIT

### git init
Initilizes and empty reposity (local)

A git project has 3 parts
1. Working Directory: where you will be doing all the work: creating, editing, deleting and organizing files
2. Staging Area: where you will list changes you make to the working directory
3. Repository: where Git permanently stores those changes as different versions of the project

Typical git workflow
edit files in 'working directory' -> adding file to the 'staging area' -> save/commit changes to repository


### git status
show the current status of the current changes

### git add <filename>
git will start tracking the changes in the file. add it to the staging area

I can call git add multiple times, each after every changes done to my file.
everyting I call the git add <file> the current changes are moved to stage.
and git diff will not show any diff after staging is done.
git diff only shows diff between the stanged file and the current file.

i.e. If I have made any changes after staging those changes alone shown in git diff

### git commit -m "<commit message>"
save the changes in the repository

### git log
It shows the history of all the commits

- A 40-character code, called a SHA, that uniquely identifies the commit. This appears in orange text.
- The commit author (you!)
- The date and time of the commit
- The commit message



# Back Tracking your repository
When working on a Git project, sometimes we make changes that we want to get rid of. Git offers a few eraser-like features that allow us to undo mistakes during project creation.

### git show HEAD
most recently done commit is known as HEAD commit.
git show HEAD displays the last commited changes

### git checkout HEAD <filename>
If some changes are made in the file and you want to revert it back to the original HEAD version, use git checkout HEAD


### git reset HEAD <file>
if you want to unstage a file from the staging area


### git reset SHA(only first 7 digit of SHA is mandatory)
If you want to remove some commits from repository use git reset.
it will remove all the latest commits after the specified SHA. and the SHA become your current HEAD



# git branching

### show your current working branch
    git branch

### create a new branch from current branch
    git branch <new branch name>
at this point the current branch and the new_branch have the same code and same number of commits. they are identical at this point.

### switched to the newly created branch
    git checkout <branch name>

### merging branch to master
    git checkout master
    git merge <branch_name>

git merge merges the changes from <branch_name> to current branch
So, if you want to merge chagnes to master then first switch to master 
    git checkout master

and now you can give git merge command to merge a branch to current branch

### merge conflict

if there is a conflict found during merging and automerge failed, git returns error and stop merging the branches. 
It specifies which file has conflicting changes and mark the conflict inside the file with following marks -
<<<<<<< HEAD [destination branch]
=======
>>>>>>> <source branch>

resolve the conflict manually
commit the changes in the conflicting file to destination_branch
and now issue the 'git merge' again

### Deleting a branch

goal of a branch is usually to 
- develop some feature
- or bug fixes 
- and then merge back to the source_branch
- then the branch can be deleted

    git branch -d <branch_name>




# Git Teamwork
how multiple users can work together for the same project
'remotes' is the collaborative repository to help this.

Normal team workflow is -
1. clone a remote_repo (origin) to my local machine (local/master)
2. create a new branch from local/master to start working with some feature
3. commit all my changes to local/my_local_branch
4. merge my_local_branch to local/master and del my_local_branch
Now my changes are done. and its present with local/master. next step is push all my changes to remote repo(origin). But before push we need to make sure my local repo is in sync with all the changes from origin.
5. fetch all the latest changes from remote origin (By this time it is hightly expected that the remote origin is advanced by several commits by the other team members)
6. all the changes from origin is saved in origin/master branch
7. merge origin/master to local/master
8. push local/master to origin

## clone a remote repo

    git clone <remote repo> <clone repo name>

clone a remote repository to my local machine. after cloning the
local clone repo become a exact replica of the remote repo

<remote repo> = web address (http://gitHub.com/remote_repo.git)

the remote_repo is termed as 'origin' by git now to keep track of the original remote repository address

    git remote -v

shows the list of git project s remotes repo addresses info

## Remote_repo(origin) is modified, how to get my_repo(cloned) updated

    git fetch

- if origin is updated 'git fetch' will shows it.
- 'git fetch' will not merge the changes from origin to local
- it fetches all the changes to a new branch called 'remote branch' or 'origin/master'
- 'local/master' branch is not updated yet
- to merge 'origin/master' changes to 'local/master' use the command
    git merge origin/master
now you have all the changes merged from origin to your local repo

## Push local repo to remote (origin)

    git push origin <my_local_branch>

I can push my local branch to origin, in case I want my team members to see my work, and if needed
it can be directly merged to the remote repo by them.

you can also push your local branch too to the origin. Then after this you can see your branch appear in the
remote repo. there in the remote repo you can now generate a new merge request for you branch to master, and 
raise a review request for this merge request towards the remote repo admin. the remote repo admin can review the
merge request and accept it. once accepted this get merged to the remote master branch.
















