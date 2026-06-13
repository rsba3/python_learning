class Driver:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

driver = Driver("Rostislavs")

driver.greet()
