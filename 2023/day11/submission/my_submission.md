Day 11 Task: Advance Git & GitHub for DevOps Engineers: Part-2

Git Stash:

Git stash is a command that allows you to temporarily save changes you have made in your working directory, without committing them. This is useful when you need to switch to a different branch to work on something else, but you don't want to commit the changes you've made in your current branch yet.

To use Git stash, you first create a new branch and make some changes to it. Then you can use the command git stash to save those changes. This will remove the changes from your working directory and record them in a new stash. You can apply these changes later. git stash list command shows the list of stashed changes.

You can also use git stash drop to delete a stash and git stash clear to delete all the stashes.

Cherry-pick:

Git cherry-pick is a command that allows you to select specific commits from one branch and apply them to another. This can be useful when you want to selectively apply changes that were made in one branch to another.

To use git cherry-pick, you first create two new branches and make some commits to them. Then you use git cherry-pick <commit_hash> command to select the specific commits from one branch and apply them to the other.

Resolving Conflicts:

Conflicts can occur when you merge or rebase branches that have diverged, and you need to manually resolve the conflicts before git can proceed with the merge/rebase. git status command shows the files that have conflicts, git diff command shows the difference between the conflicting versions and git add command is used to add the resolved files.

Task-01

Create a new branch and make some changes to it.

<img width="383" alt="create new branch" src="https://user-images.githubusercontent.com/124788172/221583869-7d29ab2c-ea40-4839-bfda-cccf4dcd11ce.png">

<img width="447" alt="changes in new branch" src="https://user-images.githubusercontent.com/124788172/221584230-8d57a11f-1f99-4a5a-a35d-86da7637492c.png">


Use git stash to save the changes without committing them.

<img width="577" alt="using git stash" src="https://user-images.githubusercontent.com/124788172/221584532-f7d72d1d-93ee-4189-aa23-c2abfa1e3c39.png">


Switch to a different branch, make some changes and commit them.

<img width="443" alt="changes and commit in dev branch" src="https://user-images.githubusercontent.com/124788172/221584985-3d910ac0-630c-40de-b5f6-03ed8c9bc3b9.png">


Use git stash pop to bring the changes back and apply them on top of the new commits.

<img width="566" alt="stash pop" src="https://user-images.githubusercontent.com/124788172/221585327-b8388960-61c3-427a-ac82-b09692be4bb3.png">


Task-02

In version01.txt of development branch add below lines after “This is the bug fix in development branch” that you added in Day10 and reverted to this commit.

Line2>> After bug fixing, this is the new feature with minor alteration”

Commit this with message “ Added feature2.1 in development branch”

<img width="548" alt="added line 2 in version in dev branch" src="https://user-images.githubusercontent.com/124788172/221586074-5b879df5-a224-4fbf-8193-58ff7f9b5176.png">



Line3>> This is the advancement of previous feature

Commit this with message “ Added feature2.2 in development branch”

<img width="562" alt="added lin 3 in dev version" src="https://user-images.githubusercontent.com/124788172/221586735-80482662-c2d8-4e75-bb76-0bee8b70239d.png">


Line4>> Feature 2 is completed and ready for release

Commit this with message “ Feature2 completed”

<img width="475" alt="line 4 added in dev ver" src="https://user-images.githubusercontent.com/124788172/221587125-cca418e3-6c04-43b6-9d5d-4c87b5793aae.png">

<img width="548" alt="log in dev" src="https://user-images.githubusercontent.com/124788172/221587604-a5e8e704-1f28-480d-bbdf-9e1d0c21e5c1.png">


All these commits messages should be reflected in Production branch too which will come out from Master branch (Hint: try rebase).

<img width="550" alt="checkout production from main" src="https://user-images.githubusercontent.com/124788172/221588248-a003ba67-54b1-479e-9fc7-0acb11254cdf.png">

<img width="1049" alt="rebase dev" src="https://user-images.githubusercontent.com/124788172/221588900-1dff2d6d-b1c2-47ed-ac5a-42ab62c08063.png">

<img width="445" alt="rebase skip" src="https://user-images.githubusercontent.com/124788172/221589117-9c48efee-2ee0-4943-a547-95b64ba12bfd.png">


Task-03

In Production branch Cherry pick Commit “Added feature2.2 in development branch” and added below lines in it:

<img width="412" alt="git log before cherry" src="https://user-images.githubusercontent.com/124788172/221589925-8d7f8000-55b8-401b-a4e6-737cabf85a30.png">

<img width="541" alt="git cherry pick in prod" src="https://user-images.githubusercontent.com/124788172/221590388-86ca4fcc-4d89-4f77-8a90-f52695d7c569.png">

<img width="536" alt="log after cherry" src="https://user-images.githubusercontent.com/124788172/221590623-583e0c08-c07a-4855-bac9-bd80241f2bbc.png">


Line to be added after Line3>> This is the advancement of previous feature

Line4>>Added few more changes to make it more optimized.

Commit: Optimized the feature

<img width="521" alt="commit after lines" src="https://user-images.githubusercontent.com/124788172/221591004-19cf17e6-ade1-4ffa-9e2a-74d43d62a7b7.png">


Reference video
