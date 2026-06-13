import json

with open("driver.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["age"])