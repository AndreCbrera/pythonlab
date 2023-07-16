class Dog:
    
    # Class attribute
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 15)

print(buddy.name, buddy.age, buddy.species)

# We an change the value
miles.species = "Felis silvestris"

print(miles.name, miles.age, miles.species)