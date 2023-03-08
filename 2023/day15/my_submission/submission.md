## Day 15 Task: Python Libraries for DevOps


## Tasks
1. Create a Dictionary in Python and write it to a json File.
```
import json

DevOps_tools = {
    1:"Linux",
    2:"AWS",
    3:"python",
    4:"Kubernetes"
}

json_file = json.dumps(DevOps_tools, indent=4) #using json.dumps() to converst python to json #indent used to give space
print(json_file)

```

2. Read a json file `services.json` kept in this folder and print the service names of every cloud service provider.

```
output

aws : ec2
azure : VM
gcp : compute engine

```
3. Read YAML file using python, file `services.yaml` and read the contents to convert yaml to json

#Refernce site
https://www.programiz.com/python-programming/json