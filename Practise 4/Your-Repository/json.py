#example 1
import json  

data = {"name": "Aibyn", "age": 17}  
json_data = json.dumps(data)  

print(json_data)
#example 2
import json  

json_string = '{"name": "Aibyn", "age": 17}'  
data = json.loads(json_string)  

print(data["name"])
#example 3
import json  

data = {"city": "Almaty"}  

with open("data.json", "w") as file:  
    json.dump(data, file)
#example 4
import json  

with open("data.json", "r") as file:  
    data = json.load(file)  

print(data)
#example 5
import json  

data = {"name": "Aibyn", "skills": ["Python", "Math"]}  
print(json.dumps(data, indent=4))