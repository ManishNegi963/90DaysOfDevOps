# Read a json file `services.json` kept in this folder and print the service names of every cloud service provider.

import json

json_file = "services.json"
with open(json_file, 'r') as f:
    data= json.load(f)

print(data)