class Truck:
    def move(self):
        print("Truck moving")

class Forklift:
    def move(self):
        print("Forklift moving")

vehicles = [Truck(), Forklift()]

for vehicle in vehicles:
    vehicle.move()