# Day 6 Task: File Permissions and Access Control Lists

1) Create a simple file and do `ls -ltr` to see the details of the files [refer to Notes](https://github.com/LondheShubham153/90DaysOfDevOps/tree/master/2023/day6/notes)
 
 Each of the three permissions are assigned to three defined categories of users. The categories are:
-	   owner   —   The owner of the file or  application.
-	"chown" is used to change the ownership permission of a file or directory.
-	   group   —   The group that owns the file or application.
-	"chgrp" is used to change the gropu permission of a file or directory.
-	   others  —   All users with access to the system. (outised the users are in a group)
-	"chmod" is used to change the other users permissions of a file or directory.

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
setfacl -m u:root:rwx Devops - will give root user to read , wrote and execute permission.