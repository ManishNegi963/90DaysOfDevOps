# Day 34 Task: Working with Services in Kubernetes

### Congratulation🎊 on your learning on Deployments in K8s on Day-33

## What are Services in K8s

In Kubernetes, Services are objects that provide stable network identities to Pods and abstract away the details of Pod IP addresses. Services allow Pods to receive traffic from other Pods, Services, and external clients.

## Task-1:

- Create a Service for your todo-app Deployment from Day-32
- Create a Service definition for your todo-app Deployment in a YAML file.

      vim service.yml

  <img width="249" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/ceec2615-4755-4a80-b058-f034a3dd62bb">

  
- Apply the Service definition to your K8s (minikube) cluster using the `kubectl apply -f service.yml -n <namespace-name>` command.

      kubectl apply -f service.yml

  <img width="554" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/d2f8870d-99d6-4068-b7e8-162a31ccd8c2">

  
- Verify that the Service is working by accessing the todo-app using the Service's IP and Port in your Namespace.

      kubectl get service -n django-ns

  <img width="630" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/804d13cb-5ecf-4cbd-af34-b5a828535262">

- verfying that sevice is able to access the application.

      minkube ssh

  <img width="583" alt="image" src="https://github.com/ManishNegi963/90DaysOfDevOps/assets/124788172/a74faa78-7fb4-406c-b9d9-a6190b6d4514">



## Task-2:

- Create a ClusterIP Service for accessing the todo-app from within the cluster
- Create a ClusterIP Service definition for your todo-app Deployment in a YAML file.
- Apply the ClusterIP Service definition to your K8s (minikube) cluster using the `kubectl apply -f cluster-ip-service.yml -n <namespace-name>` command.
- Verify that the ClusterIP Service is working by accessing the todo-app from another Pod in the cluster in your Namespace.

## Task-3:

- Create a LoadBalancer Service for accessing the todo-app from outside the cluster
- Create a LoadBalancer Service definition for your todo-app Deployment in a YAML file.
- Apply the LoadBalancer Service definition to your K8s (minikube) cluster using the `kubectl apply -f load-balancer-service.yml -n <namespace-name>` command.
- Verify that the LoadBalancer Service is working by accessing the todo-app from outside the cluster in your Namespace.

Struggling with Services? Take a look at this video for a step-by-step [guide](https://youtu.be/OJths_RojFA).

Need help with Services in Kubernetes? Check out the Kubernetes [documentation](https://kubernetes.io/docs/concepts/services-networking/service/) for assistance.

Happy Learning :)

[← Previous Day](../day33/README.md) | [Next Day →](../day35/README.md)
