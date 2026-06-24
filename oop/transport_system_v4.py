from dataclasses import dataclass

@dataclass
class Driver:
    name: str
    age: int
    license_category: str

    def __str__(self):
        return (
            f"Driver: {self.name}, "
            f"age: {self.age}, "
            f"license: {self.license_category}"
        )

@dataclass
class Car:
    brand: str
    model: str
    year: int


driver1 = Driver("Rostislavs", 30, "C/CE")
car1 = Car("BMW", "5", 2022)

print(driver1)
print(driver1.name)
print(driver1.age)
print(driver1.license_category)
print(car1)