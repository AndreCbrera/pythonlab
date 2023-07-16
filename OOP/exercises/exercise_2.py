"""
Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.
"""

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __str__(self):
        return f"Vehicle Name: School {self.name} Speed: {self.max_speed} Mileage: {self.mileage}"

volvo = Bus("Volvo", 180, 12)

print(volvo)