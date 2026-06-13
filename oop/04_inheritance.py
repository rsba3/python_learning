class Employee:
    def work(self):
        print("Working")

class Driver(Employee):
    pass

driver = Driver()

driver.work()
