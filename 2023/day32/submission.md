## Day 32 Task: Launching your Kubernetes Cluster with Deployment

### Congratulation ! on your learning on K8s on Day-31

## What is Deployment in k8s

A Deployment provides a configuration for updates for Pods and ReplicaSets.

You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate. You can define Deployments to create new replicas for scaling, or to remove existing Deployments and adopt all their resources with new Deployments.

## Today's task let's keep it very simple.

## Task-1:

**Create one Deployment file to deploy a sample todo-app on K8s using "Auto-healing" and "Auto-Scaling" feature**

- add a deployment.yml file (sample is kept in the folder for your reference)
- apply the deployment to your k8s (minikube) cluster by command
  `kubectl apply -f deployment.yml`

## Creating namespace.

    -  kubectl create namespace django-ns


  <img width="607" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/7aa53c6a-8c4b-4f3f-acb9-54a009733ced">

  
  ## View namespace.
  
    -  kubectl get namespace
 

  <img width="560" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/a828240b-d4da-4be7-9d26-4fdf3e0fb58e">


  ## Create deployment.yaml and view.

    - vim deployment.yaml 

    - cat deployment.yaml
  

<img width="437" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/e41cace8-9559-42b9-a58f-7a47c6d4b47c">


## Applying the configuration od deployment.yaml file.

    - kubectl apply -f deployment.yaml
  

<img width="604" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/e787fee2-f635-4944-8891-5662610465a2">

## View pods created with deployment file

    - kubectl get pods -n django-ns

<img width="569" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/525de3b7-b3e9-4b82-85b9-ccdd94f2ab20">


## Deleting a pod

    - kubectl delete pod django-deployment-6fcf5458b5-4tzqx  -n django-ns
  

<img width="837" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/c8d4675b-6d52-4793-b7ed-d8b0b8e9590a">

## View pods

    - kubectl get pods -n django-ns : 
  (One pod is terminating and another pod is creating automatically to get the desired state (3 pods) mentioned in the deployment, and this feature is called "Auto Healing")
  

<img width="606" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/f1a815fd-05d7-4143-b545-635e0c75586b">

## Changing the replicas to 4 in the deployment"

    - vim deployment.yaml

    - cat deployment.yaml
  

<img width="503" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/bafb4886-278a-47d3-b37d-7030f01c6227">


## Apply the edited deployment

    - kubectl apply -f deployment.yaml
  

<img width="585" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/d0e98f6c-d0d1-44e7-85c8-9f5da1d8f78e">

## View pods

    - kubectl get pods -n django-ns: 
  (Pods have been scaled to the desired state (4 pods) mentioned in the deployment file.
  

<img width="601" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/4cf01c05-0ad6-4d96-93f3-7282b3f31b12">







Let's make your resume shine with one more project ;)

**Having an issue? Don't worry, adding a sample deployment file , you can always refer that or wathch [this video](https://youtu.be/ONrbWFJXLLk)**

Happy Learning :)
