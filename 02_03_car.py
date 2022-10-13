# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car():

    def __init__(self, name, model, year, max_speed):
        self.name = name 
        self.model = model 
        self.year = year
        self.max_speed = max_speed

    def accelerate(self):
        self.max_speed = self.max_speed + 5
        print(f"the car has been tuned and its max speed increasesd by 5. the new max speed is {self.max_speed}")

    def details(self):
        print(f"this is a {self.name}, from the year {self.year}. its top speed is {self.max_speed} ")

m = Car("mercedes", "G63", 2022, 220)
t = Car("toyota", "camry", 2022, 240)

m.details()
m.accelerate()
