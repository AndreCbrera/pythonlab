"""
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

jaguar = Vehicle(max_speed="200kmh", mileage=20_000)

print(f"The Jaguar max speed is {jaguar.max_speed} per {jaguar.mileage:,}.")