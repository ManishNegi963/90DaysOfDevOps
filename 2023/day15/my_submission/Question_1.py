# Create a Dictionary in Python and write it to a json File.
import json

DevOps_tools = {
    1:"Linux",
    2:"AWS",
    3:"python",
    4:"Kubernetes"
}

json_file = json.dumps(DevOps_tools, indent=4) #using json.dumps() to converst python to json #indent used to give space
print(json_file)


