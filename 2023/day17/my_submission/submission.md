## Day 17 Task: Docker Project for DevOps Engineers.

# Dockerfile

Docker is a tool that makes it easy to run applications in containers. Containers are like small packages that hold everything an application needs to run. To create these containers, developers use something called a Dockerfile.

A Dockerfile is like a set of instructions for making a container. It tells Docker what base image to use, what commands to run, and what files to include. For example, if you were making a container for a website, the Dockerfile might tell Docker to use an official web server image, copy the files for your website into the container, and start the web server when the container starts.

For more about Dockerfile visit [here](https://rushikesh-mashidkar.hashnode.dev/dockerfile-docker-compose-swarm-and-volumes)

task:

- Create a Dockerfile for a simple web application (e.g. a Node.js or Python app)

vi Dockerfile to create a Dockerfile and then enter the commands

```

FROM python:3
RUN pip install django==3.2

COPY . .

RUN python manage.py migrate

CMD ["python","manage.py","runserver","0.0.0.0:8001"]

```

- Build the image using the Dockerfile and run the container

```

sudo docker build . -t todo-app

sudo docker run -d -p 8001:8001 865efc65ac7c

```

- Verify that the application is working as expected by accessing it in a web browser



- Push the image to a public or private repository (e.g. Docker Hub )

```

 sudo docker push todo-app

```

For Refference Project visit [here](https://youtu.be/Tevxhn6Odc8)

If you want to dive further, Watch [bootcamp](https://youtube.com/playlist?list=PLlfy9GnSVerRqYJgVYO0UiExj5byjrW8u) 

Happy Learning:)

