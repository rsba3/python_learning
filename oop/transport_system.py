class Driver:
    def __init__(self, name):
        self.name = name

class Truck:
    def __init__(self, brand):
        self.brand = brand

class Customer:
    def __init__(self, name):
        self.name = name

class Order:
    def __init__(self, order_number):
        self.order_number = order_number

driver = Driver("Rostislavs")
truck = Truck("Volvo")
customer = Customer("IKEA")
order = Order("ORD001")

print(driver.name)
print(truck.brand)
print(customer.name)
print(order.order_number)
