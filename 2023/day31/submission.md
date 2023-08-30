## Day 31 Task: Launching your First Kubernetes Cluster with Nginx running

### Awesome! You learned the architecture of one of the top most important tool "Kubernetes" in your previous task.

## What about doing some hands-on now?

Let's read about minikube and implement _k8s_ in our local machine

1. **What is minikube?**

_Ans_:- Minikube is a tool which quickly sets up a local Kubernetes cluster on macOS, Linux, and Windows. It can deploy as a VM, a container, or on bare-metal.

Minikube is a pared-down version of Kubernetes that gives you all the benefits of Kubernetes with a lot less effort.

This makes it an interesting option for users who are new to containers, and also for projects in the world of edge computing and the Internet of Things.

2. **Features of minikube**

_Ans_ :-

(a) Supports the latest Kubernetes release (+6 previous minor versions)

(b) Cross-platform (Linux, macOS, Windows)

(c) Deploy as a VM, a container, or on bare-metal

(d) Multiple container runtimes (CRI-O, containerd, docker)

(e) Direct API endpoint for blazing fast image load and build

(f) Advanced features such as LoadBalancer, filesystem mounts, FeatureGates, and network policy

(g) Addons for easily installed Kubernetes applications

(h) Supports common CI environments

## Task-01:

## Install minikube on your local

Update the system.

sudo apt update

<img width="495" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/87ae8030-8d87-4e64-b413-b7a06637aeb5">


Installing docker on local

sudo apt install -y docker.io

<img width="483" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/637472bc-4975-4699-87a7-c332556b2205">


Start docker.

sudo systemctl start docker

-Error as ubuntu is running on windows.

<img width="601" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/6dc6244c-224e-47d1-90f0-4885f44fa6e9">


Run commands to fix the errors.

sudo -b unshare --pid --fork --mount-proc /lib/systemd/systemd --system-unit=basic.target

sudo -E nsenter --all -t $(pgrep -xo systemd) runuser -P -l $USER -c "exec $SHELL"

<img width="733" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/5a20723b-7f4f-4f04-a3d8-9839d06fe6be">


Start docker.

sudo systemctl start docker

<img width="389" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/6cfefaf6-065b-4290-b456-d45e01931150">



Enable docker everytime system restarts

sudo systemctl enable docker

<img width="406" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/95e134a0-4c21-4545-a5d0-e94e5e2c6b52">


Adding current user to docker group to prevent permission denied error.

sudo usermod -aG docker $USER and newgrp docker

sudo reboot

<img width="486" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/c0e34b88-d7f7-44a4-9137-9db077beb03a">


Downloading minicube.

curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

<img width="785" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/1daad3dd-bbf9-4853-8c87-adc86bb5544a">


List all the files.

ls : minikube file has been downloaded

<img width="495" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/7c0923fc-5908-46d3-8ee8-61d6f85cd504">


Changing file permission to make it executable and moving the file minikube to bin folder

chmod +x minikube

sudo mv minikube /usr/local/bin/

<img width="355" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/3b25b1ec-3f5f-42e3-9b23-5986fdb17b3b">


Check minikube is working.

<img width="662" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/db9879c5-dd1d-4a88-822a-8762b36f1979">


Download kubectl

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

<img width="850" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/28e58a0c-14a6-47a9-91a9-6b5f567f2e8a">


Changing kubectl file permission to be executable and moving it to bin folder.

chmod +x kubectl

sudo mv kubectl /usr/local/bin/

<img width="851" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/dc33712b-6cad-4947-a03c-c45e6bf37633">


Start minicube.

minikube start --driver=docker

<img width="695" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/e452a124-5d0f-4148-900f-00795342c7b5">


View all the running container.

docker ps: minicube container is running.

<img width="856" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/e37629a8-7a6a-449c-9142-3ed2b828c078">


GO inside the minikube container and view all the container.

minikube ssh :to go inside the minikube container

docker ps : view all the running container in minikube

<img width="863" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/bb5364c5-b053-463c-8b50-ab6949aa0182">


To view all the nodes

kubectl get nodes

<img width="418" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/51a14b28-fc7c-4135-9e6c-b6b1bb9e0571">


To view the pods.

kubectl get pods

<img width="335" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/c979d6ac-29b8-4fe8-ad1f-5d4e3589562b">


## Task-02:

## Create your first pod on Kubernetes through minikube.


Create a namespace.

kubectl create namespace react-django-ns

<img width="404" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/bf97640c-d2ef-4798-b5db-beb684c42c19">


To view namespaces.

kubectl get namespaces

<img width="575" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/377edff4-0093-478e-8371-cf2d864f65fc">



Creating a directory and create a pod.yaml file

mkdir django-project-k8

touch pod.yaml

<img width="447" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/57cd61be-4a3f-4a2f-9af7-8ede1c8de1a9">


vim pod.yaml and cat pod.yaml

apiVersion: v1
kind: Pod
metadata:
  name: django
  namespace: react-django-ns
spec:
  containers:
  - name: django-ctr
    image: django
    ports:
    - containerPort: 80

<img width="371" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/8348da99-782c-4468-9a87-8cde1d5ebac6">


Create pod from pod.yaml file

kubectl apply -f pod.yaml

<img width="484" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/8bb4d77b-c8bb-4ac1-88d3-293ebb67186e">


To view the pods.

kubectl get pods : As no pods are created in default namespace

<img width="488" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/a341b4a9-8e0b-473d-967e-1e49cee64ab1">


kubectl get pods --namespace=react-django-ns

<img width="616" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/423ae9f6-5dad-499f-a81a-980acfe31e49">


To view the IP address of the pod.

kubectl get pods --namespace=react-django-ns -o wide

<img width="818" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/3e5ee1be-f1a1-490f-a95c-c34c6d46c0bc">


To view the detailed information of the pod.

kubectl describe pod --namespace=react-django-ns 

<img width="712" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/7af3ab38-a01d-4eeb-bb58-32fb59c5809b">


To delete the pod.

kubectl delete pod --namespace=react-django-ns



For installation, you can Visit [this page](https://minikube.sigs.k8s.io/docs/start/).

If you want to try an alternative way, you can check [this](https://k8s-docs.netlify.app/en/docs/tasks/tools/install-minikube/).

## Let's understand the concept **pod**

_Ans:-_

Pods are the smallest deployable units of computing that you can create and manage in Kubernetes.

A Pod (as in a pod of whales or pea pod) is a group of one or more containers, with shared storage and network resources, and a specification for how to run the containers. A Pod's contents are always co-located and co-scheduled, and run in a shared context. A Pod models an application-specific "logical host": it contains one or more application containers which are relatively tightly coupled.

You can read more about pod from [here](https://kubernetes.io/docs/concepts/workloads/pods/) .

## Installation of minikube on local.

_Happy Learning :)_
