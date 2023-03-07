
"""
Create below Dictionary and use Dictionary methods to print your favourite tool just by using the keys of the Dictionary.
```
fav_tools = 
{ 
  1:"Linux", 
  2:"Git", 
  3:"Docker", 
  4:"Kubernetes", 
  5:"Terraform", 
  6:"Ansible", 
  7:"Chef"
}

"""

fav_tools = { 
              1:"Linux",
              2:"Git", 
              3:"Docker", 
              4:"Kubernetes", 
              5:"Terraform", 
              6:"Ansible",
              7:"Chef"
            }

print(fav_tools.get(1))