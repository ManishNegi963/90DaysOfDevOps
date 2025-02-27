# Day 10 Task: Advance Git & GitHub for DevOps Engineers.

## Git Branching
 Use a branch to isolate development work without affecting other branches in the repository. Each repository has one default branch, and can have multiple other branches. You can merge a branch into another branch using a pull request.

 Branches allow you to develop features, fix bugs, or safely experiment with new ideas in a contained area of your repository.

## Git Revert and Reset
 Two commonly used tools that git users will encounter are those of git reset and git revert . The benefit of both of these commands is that you can use them to remove or edit changes you’ve made in the code in previous commits.

## Git Rebase and Merge
 ### What Is Git Rebase?

 Git rebase is a command that lets users integrate changes from one branch to another, and the logs are modified once the action is complete. Git rebase was developed to overcome merging’s shortcomings, specifically regarding logs.

 ### What Is Git Merge?

 Git merge is a command that allows developers to merge Git branches while the logs of commits on branches remain intact.

 The merge wording can be confusing because we have two methods of merging branches, and one of those ways is actually called “merge,” even though both procedures do essentially the same thing.

 Refer to this article for a better understanding of Git Rebase and Merge [Read here](https://www.simplilearn.com/git-rebase-vs-merge-article)


## Task 1:
 Add a text file called version01.txt inside the Devops/Git/ with “This is first feature of our application” written inside. 
 This should be in a branch coming from `master`, 
 [hint try `git checkout -b dev`], 
 swithch to `dev` branch ( Make sure your commit message will reflect as "Added new feature").
 [Hint use your knowledge of creating branches and Git commit command]
 
 <img width="742" alt="created version file in dev" src="https://user-images.githubusercontent.com/124788172/221428515-87906fc0-2728-48f2-8e8b-6ce420b3ad93.png">

<img width="341" alt="create log" src="https://user-images.githubusercontent.com/124788172/221428529-4e9b009c-796c-4dd5-95db-771ec5ec2180.png">

 - version01.txt should reflect at local repo first followed by Remote repo for review.
 [Hint use your knowledge of Git push and git pull commands here] 
 
 <img width="399" alt="push dev" src="https://user-images.githubusercontent.com/124788172/221428554-a523a855-fba4-4577-bb45-94773e647e46.png">


 Add new commit in `dev` branch after adding below mentioned content in Devops/Git/version01.txt:
 While writing the file make sure you write these lines
 
 - 1st line>>  This is the bug fix in development branch
 - Commit this with message “ Added feature2 in development branch”

<img width="543" alt="added feature 2" src="https://user-images.githubusercontent.com/124788172/221428575-b580fbb0-86d4-4fae-b32b-49b2b7d45051.png">

 
 - 2nd line>> This is gadbad code
 - Commit this with message “ Added feature3 in development branch

<img width="552" alt="added feature 3" src="https://user-images.githubusercontent.com/124788172/221428589-5387eda3-a64c-4382-b103-869f518bece2.png">

 
 - 3rd line>> This feature will gadbad everything from now.
 - Commit with message “ Added feature4 in development branch

<img width="541" alt="added feature 4" src="https://user-images.githubusercontent.com/124788172/221428595-f8ac001f-c1a7-4ed4-acf8-a5b5c957f0ad.png">

<img width="439" alt="git log " src="https://user-images.githubusercontent.com/124788172/221428603-ba096835-ef9a-4bcd-a0cc-441845d1fd0c.png">

 Restore the file to a previous version where the content should be “This is the bug fix in development branch”
 [Hint use git revert or reset according to your knowledge]
 
 <img width="450" alt="git revert 1" src="https://user-images.githubusercontent.com/124788172/221428615-6e800e11-6346-4ea7-a192-97bc0526dd29.png">
<img width="463" alt="git revert 2" src="https://user-images.githubusercontent.com/124788172/221428623-73024af3-ffdf-432f-b516-bc72fcc6bc36.png">
<img width="544" alt="git revert to first" src="https://user-images.githubusercontent.com/124788172/221428626-e7143fb4-b730-47a1-aca6-2996135aa505.png">


## Task 2:

 - Demonstrate the concept of branches with 2 or more branches with screenshot.

Command to know the current branch 

<img width="344" alt="branches" src="https://user-images.githubusercontent.com/124788172/221430787-d5a31e6b-b911-46b1-8f69-878bb0b6014e.png">

Dev branch

<img width="445" alt="dev branch" src="https://user-images.githubusercontent.com/124788172/221430939-27488648-7ad1-4fff-86f5-fc960f2d9c60.png">

Main Branch

<img width="371" alt="main branch" src="https://user-images.githubusercontent.com/124788172/221430953-38fdbe33-319d-408d-847e-223366833864.png">


 - add some changes to `dev` branch and merge that branch in `master`

<img width="353" alt="added" src="https://user-images.githubusercontent.com/124788172/221431349-d5382e21-2035-4f23-9989-4542912cc8ff.png">



 - as a practice try git rebase too, see what difference you get.

Log of Main branch

<img width="550" alt="main log" src="https://user-images.githubusercontent.com/124788172/221432634-3d7d24f7-6fb2-40a4-bf3f-e6bb515670e8.png">

Checkout feature00 branch from log 976e7f5 of main branch and created file feature01.txt and commit.

<img width="491" alt="feature00 and file feature01" src="https://user-images.githubusercontent.com/124788172/221432727-1675901f-ce0c-4f4c-bed3-d4569fdcc82f.png">

Log of feature00 branch

<img width="415" alt="feature log" src="https://user-images.githubusercontent.com/124788172/221432751-7a14d331-2607-461f-8767-75bcec7a060a.png">

Rebase main branch in feature branch and see the log, feature01.txt has been added to main branch

<img width="547" alt="rebase main in feature branch" src="https://user-images.githubusercontent.com/124788172/221432772-a75e2799-74d3-4868-89fc-df6dfb50cdff.png">

Rebase feature00 in main branch by switching to main branch and see logs that commits of feature00 branch has been added to main branch


<img width="524" alt="rebase feature00 in main" src="https://user-images.githubusercontent.com/124788172/221432854-0eb9f8dc-ca93-4dde-ad01-1102b930cb96.png">






