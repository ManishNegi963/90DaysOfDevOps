# Day 5 Task: Advanced Linux Shell Scripting for DevOps Engineers with User management

- Write a bash script createDirectories.sh that when the script is executed with three given arguments (one is directory name and second is start number of directories and third is the end number of directories ) it creates specified number of directories with a dynamic directory name.


- Create a Script to backup all your work done till now.


- Read About Cron and Crontab, to automate the backup Script.
Cron is a linux utility to schedule the task to be automatically execute.

A crontab is a text file containing the commands to be executed at partiular time automatically.

Crontab can be scheduled by specifying the following:
Minutes(0-59) Hours(0-23) Day of the month(1-31) Month(1-12) Day of the week(0-7,where 0 and 7 both represent sunday) command to be executed

crontab -e can be used to edit the file and crontab -l to list all the crontab files 

- Read about User Management
User management in Linux mainly involves three administrative tasks adding, modifying and removing user accounts.

Commands for user management includes:
useradd, usermod, userdel, passwd and groupadd, groupdel, groupmod

- Create 2 users and just display their Usernames
