from os import name


class Driver:
    def __init__(self, name, age, license_category):
        self.name = name
        self.age = age
        self.license_category = license_category

    def info(self):
        print(
            f"Driver: {self.name}, "
            f"age: {self.age}, "
            f"license: {self.license_category}"
        )

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "license_category": self.license_category
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["age"],
            data["license_category"]
        )

    def __str__(self):
        return(
            f"Driver: {self.name}, "
            f"age: {self.age}, "
            f"license: {self.license_category}"
        )


class Truck:
    def __init__(self, brand, model, max_weight):
        self.brand = brand
        self.model = model
        self.max_weight = max_weight

    def info(self):
        print(
            f"Truck: {self.brand} {self.model}, "
            f"max weight: {self.max_weight} kg"
        )

    def to_dict(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "max_weight": self.max_weight
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["brand"],
            data["model"],
            data["max_weight"]
        )


class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def info(self):
        print(f"Customer: {self.name}, city: {self.city}")

    def to_dict(self):
        return {
            "name": self.name,
            "city": self.city
            }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["city"]
            )


class Order:
    def __init__(self, driver, truck, customer, destination, cargo_weight):
        self.driver = driver
        self.truck = truck
        self.customer = customer
        self.destination = destination
        self.cargo_weight = cargo_weight

    def info(self):
        print("Order information")
        print(f"Driver: {self.driver.name}")
        print(f"Truck: {self.truck.brand}, {self.truck.model}")
        print(f"Customer: {self.customer.name}")
        print(f"Destination: {self.destination}")
        print(f"Cargo weight: {self.cargo_weight}kg")

    def to_dict(self):
        return {
            "driver": self.driver.to_dict(),
            "truck": self.truck.to_dict(),
            "customer": self.customer.to_dict(),
            "destination": self.destination,
            "cargo_weight": self.cargo_weight()
        }

    @classmethod
    def from_dict(cls, data):
        driver = Driver.from_dict(data["driver"])
        truck = Truck.from_dict(data["truck"])
        customer = Customer.from_dict(data["customer"])

        return cls(
            driver,
            truck,
            customer,
            data["destination"],
            data["cargo_weight"]
        )

if __name__ == "__main__":
    driver1 = Driver("Rostislavs", 30, "C/CE")
    truck1 = Truck("Mercedes", "Actros", 18000)
    customer1 = Customer("PostNord", "Oslo")
    order1 = Order(driver1, truck1, customer1, "Bergen", 12000)
    customer2 = Customer("DHL", "Trondheim")
    order2 = Order(driver1, truck1, customer2, "Trondheim", 8000)

    driver1.info()
    truck1.info()
    customer1.info()
    order1.info()
    print()
    order2.info()
    print(driver1)
    driver1.to_dict()
