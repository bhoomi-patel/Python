import json
#1 save data to JSON file
data = {"name": "Alice", "age": 25, "skills":["python","ai","ml"],"is_student":True}
# save to file
with open ("person.json","w") as file:
    json.dump(data,file,indent=2)
# convert to string
json_string = json.dumps(data,indent=2)
print(json_string)

#2 load data from JSON file
with open("person.json","r" ) as file:
    loaded_data = json.load(file)
print(loaded_data)
person = json.loads(json_string)
print(person["age"])


# practice problems 
#1 filter user by age

with open("user.json") as f:
    users = json.load(f)
for i in users:
    if i.get("age") > 25 :
        print(i["name"])

#2 sort and save 
products = {"banana":1.2,"apple":2.5,"orange":1.8}
with open("catalog.json","w") as f:
    json.dump(products,f,indent=4,sort_keys=True)