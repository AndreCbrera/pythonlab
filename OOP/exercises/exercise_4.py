"""
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
"""

class Vehicle:

    # attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f"Color: {self.color} Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage:,}"

        

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

audi = Car("BMW", 190, 20_000)
volvo = Bus("Volvo", 200, 190)

for vehicle in(audi, volvo):
    print(vehicle)