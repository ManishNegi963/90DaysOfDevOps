# Day 7 Task: Understanding package manager and systemctl

## Tasks

 1) You have to install docker and jenkins in your system from your terminal using package managers.

 1. Open the terminal on Ubuntu.
 2. Remove any Docker files that are running in the system, using the following command:

$ sudo apt-get remove docker docker-engine docker.io
After entering the above command, you will need to enter the password of the root and press enter.

3. Check if the system is up-to-date using the following command:

$ sudo apt-get update

4. Install Docker using the following command:

$ sudo apt install docker.io

You’ll then get a prompt asking you to choose between y/n - choose y

5. Install all the dependency packages using the following command:

$ sudo snap install docker

6. Before testing Docker, check the version installed using the following command:

$ docker --version

7. Pull an image from the Docker hub using the following command:

$ sudo docker run hello-world
Here, hello-world is the docker image present on the Docker hub.

8. Check if the docker image has been pulled and is present in your system using the following command:

$ sudo docker images

9. To display all the containers pulled, use the following command:

$ sudo docker ps -a

10. To check for containers in a running state, use the following command:

$ sudo docker ps
You’ve just successfully installed Docker on Ubuntu!

Steps to install jenkins on Ubuntu.

Step 1 — Installing Jenkins
The version of Jenkins included with the default Ubuntu packages is often behind the latest available version from the project itself. To ensure you have the latest fixes and features, use the project-maintained packages to install Jenkins.

First, add the repository key to your system:

wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key |sudo gpg --dearmor -o /usr/share/keyrings/jenkins.gpg
The gpg --dearmor command is used to convert the key into a format that apt recognizes.

Next, let’s append the Debian package repository address to the server’s sources.list:

sudo sh -c 'echo deb [signed-by=/usr/share/keyrings/jenkins.gpg] http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
The [signed-by=/usr/share/keyrings/jenkins.gpg] portion of the line ensures that apt will verify files in the repository using the GPG key that you just downloaded.

After both commands have been entered, run apt update so that apt will use the new repository.

sudo apt update
Finally, install Jenkins and its dependencies:

sudo apt install jenkins
Now that Jenkins and its dependencies are in place, we’ll start the Jenkins server.

Step 2 — Starting Jenkins
now that Jenkins is installed, start it by using systemctl:

sudo systemctl start jenkins.service
Since systemctl doesn’t display status output, we’ll use the status command to verify that Jenkins started successfully:

sudo systemctl status jenkins
If everything went well, the beginning of the status output shows that the service is active and configured to start at boot.

## Tasks

 1) check the status of docker service in your system (make sure you completed above tasks, else docker won't be installed)
<img width="383" alt="docker " src="https://user-images.githubusercontent.com/124788172/219025178-efcb7fb8-6b46-40a4-bd90-c806efa8c21c.png">

 2) stop the service jenkins and post before and after screenshots

 3) read about the commands systemctl vs service
 systemd : It is a default init system in linux used manage and to run the services on the Linux system.
 systemctl : It is command line tool used to control, manage the systmd services and provides various commands to start, stop, enable and disable services.

 - start a service: systemctl start service-name
 - stop a service: systemctl stop service-name
 - restart a service : systemctl restart service-name
 - enable a service to automatically start at boot: systemctl enable service-name
 - disable  a service to automatically stop at boot: systemctl disable service-name
 - check the status of service: systemctl status service-name




