class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Driver: {self.name}, age: {self.age}")

class Truck:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Truck: {self.brand} {self.model}")

class Customer:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Customer: {self.name}")

class Order:
    def __init__(self, order_number, driver, truck, customer):
        self.order_number = order_number
        self.driver = driver
        self.truck = truck
        self.customer = customer

    def info(self):
        print(f"Order: {self.order_number}")
        print(f"Driver: {self.driver.name}")
        print(f"Truck: {self.truck.brand} {self.truck.model}")
        print(f"Customer: {self.customer.name}")

driver1 = Driver("Rostislavs", 30)
driver2 = Driver("John", 45)

truck1 = Truck("Volvo", "FH16")
truck2 = Truck("Scania", "R500")

customer1 = Customer("IKEA")
customer2 = Customer("Bring")

order1 = Order(
    "ORD001",
    driver1,
    truck1,
    customer1
)

order2 = Order(
    "ORD002",
    driver2,
    truck2,
    customer2
)

order1.info()
print()
order2.info()

order1.driver.name