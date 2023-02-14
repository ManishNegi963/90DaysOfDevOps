# Day 6 Task: File Permissions and Access Control Lists

1) Create a simple file and do `ls -ltr` to see the details of the files [refer to Notes](https://github.com/LondheShubham153/90DaysOfDevOps/tree/master/2023/day6/notes)
 
 <img width="373" alt="ls -ltr" src="https://user-images.githubusercontent.com/124788172/218780218-9e754866-2d69-4f25-ad14-d9dcc87c02fe.png">

 
 Each of the three permissions are assigned to three defined categories of users. The categories are:
-	   owner   —   The owner of the file or  application.

<img width="368" alt="chown" src="https://user-images.githubusercontent.com/124788172/218780272-81997258-019f-44e2-add6-0505ae38190e.png">

-	"chown" is used to change the ownership permission of a file or directory.
-	   group   —   The group that owns the file or application.
-	"chgrp" is used to change the gropu permission of a file or directory.

<img width="392" alt="chgrp" src="https://user-images.githubusercontent.com/124788172/218780329-0d7cb75c-ca60-47f8-8852-7eb12c694619.png">

-	   others  —   All users with access to the system. (outised the users are in a group)
-	"chmod" is used to change the other users permissions of a file or directory.
-	
<img width="366" alt="chmod" src="https://user-images.githubusercontent.com/124788172/218780351-3784c59d-012a-4ddf-b2f8-9efb7e053b99.png">

2) Write an article about File Permissions based on your understanding from the notes.
File permission are rights to read, write and execute the file.
w- write 
r- read
x- execute
0 - no permission
1 - execute
2 - write
4 - read
combination of these refers to the file permission.
001 - execute only
002 - write only

3) Read about ACL and try out the commands `getfacl` and `setfacl`
ACL refers to the access contol list used to view and modify the access controls of the file in Linux.
'getfacl' = refers to view the access control of the file or directory in linux.
'setfacl' = refers to modify the access control of file or directory.
for example : getfacl Devops - will deiplay the access control of the file Devops 

<img width="364" alt="getfacl" src="https://user-images.githubusercontent.com/124788172/218780468-cc323721-3833-48ca-97ff-d8f3666a2e46.png">

setfacl -m u:root:rwx Devops - will give root user to read , wrote and execute permission.
<img width="465" alt="serfacl" src="https://user-images.githubusercontent.com/124788172/218780498-565f5d5c-62ff-46d1-af17-a2e9bf694920.png">



