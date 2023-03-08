# Read YAML file using python, file `services.yaml` and read the contents to convert yaml to json


import json
import yaml 

yaml_file = "services.yaml"

with open(yaml_file, 'r') as s:
      yaml_data = yaml.safe_load(s)

print(yaml_data)

python_data=yaml_data

with open(python_data, 'r') as j:
     json_data= json.dumps(j)

print(json_data)
      


