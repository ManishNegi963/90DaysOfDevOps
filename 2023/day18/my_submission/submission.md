# Day 18 Task: Docker for DevOps Engineers

Till created Docker file and pushed it to the Repository. Let's move forward and dig more on other Docker concepts.

## Docker Compose
- Docker Compose is a tool that was developed to help define and share multi-container applications.
- With Compose, we can create a YAML file to define the services and with a single command, can spin everything up or tear it all down.
- Learn more about docker-compose [visit here](https://tecadmin.net/tutorial/docker/docker-compose/)

## What is YAML?
- YAML is a data serialization language that is often used for writing configuration files. Depending on whom you ask, YAML stands for yet another markup language or YAML ain’t markup language (a recursive acronym), which emphasizes that YAML is for data, not documents. 
- YAML is a popular programming language because it is human-readable and easy to understand.
- YAML files use a .yml or .yaml extension.
- Read more about it [here](https://www.redhat.com/en/topics/automation/what-is-yaml)

## How to run Docker commands without sudo?
- Make sure docker is installed and system is updated (This is already been completed as a part of previous tasks):
- sudo usermod -a -G docker $USER 
- Reboot the machine.

## Install Docker Compose

```

$ sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose

```

## Task-1

Learn how to use the docker-compose.yml file, to set up the environment, configure the services and links between different containers, and also to use environment variables in the docker-compose.yml file. 

[Sample docker-compose.yaml file](https://github.com/LondheShubham153/90DaysOfDevOps/blob/master/2023/day18/docker-compose.yaml)

<img width="851" alt="docker-compose install" src="https://user-images.githubusercontent.com/124788172/224453996-0c8b5ff1-bd70-4f53-88cf-3d99b71c0cd7.png">


<img width="524" alt="docker compose create n see" src="https://user-images.githubusercontent.com/124788172/224454078-443607c1-51f1-4997-b734-b70e03e297b4.png">

<img width="830" alt="docker compose run and ps" src="https://user-images.githubusercontent.com/124788172/224454090-84422c14-2d34-4ab3-a794-45b37f23f128.png">


## Task-2
- Pull a pre-existing Docker image from a public repository (e.g. Docker Hub) and run it on your local machine. Run the container as a non-root user (Hint- Use `usermod ` command to give user permission to docker). Make sure you reboot instance after giving permission to user.
- Inspect the container's running processes and exposed ports using the docker inspect command.

<img width="848" alt="docker ps and inspect" src="https://user-images.githubusercontent.com/124788172/224454155-c16d9194-40e1-42e7-b48f-e6f366215af5.png">

<img width="743" alt="docker network sett" src="https://user-images.githubusercontent.com/124788172/224454172-d8b6daeb-e9ff-4c66-b237-81093e8f9350.png">


- Use the docker logs command to view the container's log output.

<img width="847" alt="docker logs" src="https://user-images.githubusercontent.com/124788172/224454188-5bb0ce33-66bc-4c89-aac1-ddcd91157ba7.png">


- Use the docker stop and docker start commands to stop and start the container.

<img width="844" alt="docker stop n ps" src="https://user-images.githubusercontent.com/124788172/224454211-694f36e1-99a1-4195-b2d9-42cde2373949.png">

<img width="852" alt="docker start n ps" src="https://user-images.githubusercontent.com/124788172/224454217-727adecf-1d3f-49bc-8156-8b26e5fe220f.png">


- Use the docker rm command to remove the container when you're done.

<img width="851" alt="docker stop n rm n ps" src="https://user-images.githubusercontent.com/124788172/224454226-90575f8a-36a0-415a-ae22-ee6f21bb60f8.png">


For reference you can watch this [video](https://youtu.be/Tevxhn6Odc8)
