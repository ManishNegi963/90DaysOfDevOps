# Day 33 Task: Working with Namespaces and Services in Kubernetes

## What are Namespaces and Services in k8s

In Kubernetes, Namespaces are used to create isolated environments for resources. Each Namespace is like a separate cluster within the same physical cluster. Services are used to expose your Pods and Deployments to the network. Read more about Namespace [Here](https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/)

# Today's task:

## Task 1:

- Create a Namespace for your Deployment

- Use the command `kubectl create namespace <namespace-name>` to create a Namespace

      kubectl create namespace django-ns


  <img width="450" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/c56ce0e9-5b03-4ab9-bdef-f26565bbb81d">


- Update the deployment.yml file to include the Namespace


  <img width="309" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/cc13a56f-ee81-4a7f-85d5-37a58aed3ac1">


- Apply the updated deployment using the command:

      kubectl apply -f deployment.yml -n django-ns

  <img width="452" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/0f90dcf0-050c-4b86-9ff7-9a677f447bd2">


  

- Verify that the Namespace has been created by checking the status of the Namespaces in your cluster.

      kubectl get namespace

## Task 2:

- Read about Services, Load Balancing, and Networking in Kubernetes. Refer official documentation of kubernetes [Link](https://kubernetes.io/docs/concepts/services-networking/)

Need help with Namespaces? Check out this [video](https://youtu.be/K3jNo4z5Jx8) for assistance.

Keep growing your Kubernetes knowledge💥🙌

Happy Learning! :)


