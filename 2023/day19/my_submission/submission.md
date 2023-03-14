# Day 19 Task: Docker for DevOps Engineers

**Till now you have learned how to create docker-compose.yml file and pushed it to the Repository. Let's move forward and dig more on other Docker-compose.yml concepts.**
**Aaj thodi padhai krte hai on Docker Volume & Docker Network** 😃

# Docker-Volume
Docker allows you to create something called volumes. Volumes are like separate storage areas that can be accessed by containers. They allow you to store data, like a database, outside the container, so it doesn't get deleted when the container is deleted.
You can also mount from the same volume and create more containers having same data.
[reference](https://docs.docker.com/storage/volumes/)

# Docker Network
Docker allows you to create virtual spaces called networks, where you can connect multiple containers (small packages that hold all the necessary files for a specific application to run) together. This way, the containers can communicate with each other and with the host machine (the computer on which the Docker is installed).
When we run a container, it has its own storage space that is only accessible by that specific container. If we want to share that storage space with other containers, we can't do that. [reference](https://docs.docker.com/network/)


## Task-1
- Create a multi-container docker-compose file which will bring *UP* and bring *DOWN* containers in a single shot ( Example - Create application and database container )

*hints:*
- Use the `docker-compose up` command with the `-d` flag to start a multi-container application in detached mode.

<img width="566" alt="docker up" src="https://user-images.githubusercontent.com/124788172/225039387-cf93adcc-3b10-4c81-91ce-95ad3556b37d.png">


- Use the `docker-compose scale` command to increase or decrease the number of replicas for a specific service. You can also add [`replicas`](https://stackoverflow.com/questions/63408708/how-to-scale-from-within-docker-compose-file) in deployment file for *auto-scaling*.
- Use the `docker-compose ps` command to view the status of all containers, and `docker-compose logs` to view the logs of a specific service.

<img width="806" alt="dc cm ps" src="https://user-images.githubusercontent.com/124788172/225039490-547409ed-deea-4cd0-9316-470a5583f9b7.png">


- Use the `docker-compose down` command to stop and remove all containers, networks, and volumes associated with the application

<img width="710" alt="dc cm down" src="https://user-images.githubusercontent.com/124788172/225039537-cdf4f894-9bb1-47e5-9af0-fb23b86db1af.png">


## Task-2
- Learn how to use Docker Volumes and Named Volumes to share files and directories between multiple containers.

<img width="500" alt="create vol" src="https://user-images.githubusercontent.com/124788172/225039601-9562dc17-47a5-4951-964a-aacb80128159.png">

<img width="603" alt="inspect volume" src="https://user-images.githubusercontent.com/124788172/225039644-ca0cb76d-eae5-4373-8db1-70af3bfba1b9.png">

- Create two or more containers that read and write data to the same volume using the `docker run --mount` command.

<img width="856" alt="docke run" src="https://user-images.githubusercontent.com/124788172/225039709-8ba13036-0893-4e20-8bcd-95dbd7490ab8.png">


- Verify that the data is the same in all containers by using the docker exec command to run commands inside each container.


<img width="581" alt="docke exec" src="https://user-images.githubusercontent.com/124788172/225039839-6fc46633-8e87-482b-a5d2-30a198c4f929.png">


- Use the docker volume ls command to list all volumes and docker volume rm command to remove the volume when you're done.

<img width="598" alt="ocker volume ps" src="https://user-images.githubusercontent.com/124788172/225039941-3cd67937-4759-4ed7-9d2e-afee4597e494.png">

<img width="635" alt="stop n rm" src="https://user-images.githubusercontent.com/124788172/225040014-4e6e1e78-7743-4b59-8ff7-2710d41246b1.png">

<img width="566" alt="volumen rm" src="https://user-images.githubusercontent.com/124788172/225040057-a08bb12e-e1ee-4532-a0f6-0b0001948b29.png">


## You can use this task as *Project* to add in your resume.

You can Post on LinkedIn and let us know what you have learned from this task by #90DaysOfDevOps Challange. Happy Learning :)
