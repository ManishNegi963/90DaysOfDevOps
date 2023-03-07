"""
3. Create a List of cloud service providers
eg.
```
cloud_providers = ["AWS","GCP","Azure"]
```
Write a program to add `Digital Ocean` to the list of cloud_providers and sort the list in alphabetical order.

[Hint: Use keys to built in functions for Lists]

"""

# solution

cloud_providers = ["AWS","GCP","Azure"]
print(type(cloud_providers))

cloud_providers.append("Digital Ocean")
print(cloud_providers)

cloud_providers.sort()
print(cloud_providers)