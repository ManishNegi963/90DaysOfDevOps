# Day 8 Task: Basic Git & GitHub for DevOps Engineers.

## What is Git?
Git is a version control system that allows you to track changes to files and coordinate work on those files among multiple people. It is commonly used for software development, but it can be used to track changes to any set of files.

With Git, you can keep a record of who made changes to what part of a file, and you can revert back to earlier versions of the file if needed. Git also makes it easy to collaborate with others, as you can share changes and merge the changes made by different people into a single version of a file.

## What is Github?
GitHub is a web-based platform that provides hosting for version control using Git. It is a subsidiary of Microsoft, and it offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features. GitHub is a very popular platform for developers to share and collaborate on projects, and it is also used for hosting open-source projects.

## What is Version Control? How many types of version controls we have?
Version control is a system that tracks changes to a file or set of files over time so that you can recall specific versions later. It allows you to revert files back to a previous state, revert the entire project back to a previous state, compare changes over time, see who last modified something that might be causing a problem, who introduced an issue and when, and more.

There are two main types of version control systems: centralized version control systems and distributed version control systems.

1) A centralized version control system (CVCS) uses a central server to store all the versions of a project's files. Developers "check out" files from the central server, make changes, and then "check in" the updated files. Examples of CVCS include Subversion and Perforce.

2) A distributed version control system (DVCS) allows developers to "clone" an entire repository, including the entire version history of the project. This means that they have a complete local copy of the repository, including all branches and past versions. Developers can work independently and then later merge their changes back into the main repository. Examples of DVCS include Git, Mercurial, and Darcs.


## Why we use distributed version control over centralized version control? 

1) Better collaboration: In a DVCS, every developer has a full copy of the repository, including the entire history of all changes. This makes it easier for developers to work together, as they don't have to constantly communicate with a central server to commit their changes or to see the changes made by others.

2) Improved speed: Because developers have a local copy of the repository, they can commit their changes and perform other version control actions faster, as they don't have to communicate with a central server.

3) Greater flexibility: With a DVCS, developers can work offline and commit their changes later when they do have an internet connection. They can also choose to share their changes with only a subset of the team, rather than pushing all of their changes to a central server.

4) Enhanced security: In a DVCS, the repository history is stored on multiple servers and computers, which makes it more resistant to data loss. If the central server in a CVCS goes down or the repository becomes corrupted, it can be difficult to recover the lost data.

Overall, the decentralized nature of a DVCS allows for greater collaboration, flexibility, and security, making it a popular choice for many teams.

## Task:

- Install Git on your computer (if it is not already installed). You can download it from the official website at https://git-scm.com/downloads
- Create a free account on GitHub (if you don't already have one). You can sign up at https://github.com/
- Learn the basics of Git by reading through the [video](https://youtu.be/AT1uxOLsCdk) This will give you an understanding of what Git is, how it works, and how to use it to track changes to files.

## Exercises:

1) Create a new repository on GitHub and clone it to your local machine
<img width="849" alt="created github file" src="https://user-images.githubusercontent.com/124788172/219371537-6fe18f5b-1489-4066-8496-2a9845d43c85.png">
<img width="539" alt="git clone" src="https://user-images.githubusercontent.com/124788172/219371555-baba7565-0bee-4197-8c65-1610f3f845e4.png">


2) Make some changes to a file in the repository and commit them to the repository using Git
<img width="437" alt="change in gitrepo" src="https://user-images.githubusercontent.com/124788172/219371629-c6101082-ca1a-4e46-bc36-0b22ceded856.png">

<img width="403" alt="commit changes" src="https://user-images.githubusercontent.com/124788172/219371646-1b6c5591-29cb-4403-a103-c3ec8cd9c6c5.png">

3) Push the changes back to the repository on GitHub
<img width="384" alt="push changes to github" src="https://user-images.githubusercontent.com/124788172/219371702-b4c2d505-fd2c-4049-a0e7-034e285b9e2b.png">

