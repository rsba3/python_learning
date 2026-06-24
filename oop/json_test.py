import json
from transport_system_v3 import Driver

driver1 = Driver("Rostislavs", 30, "C/CE")

driver_data =driver1.to_dict()

with open("driver.json", "w") as file:
    json.dump(driver_data, file, indent=4)

with open("driver.json", "r") as file:
    data = json.load(file)

driver = Driver.from_dict(data)

driver.info()

print(data)
