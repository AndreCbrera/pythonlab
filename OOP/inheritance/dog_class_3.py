class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"


# Extended functionality from parent class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says: {sound}"

# Access to parent calls speak method
class Dachshund(Dog):
    def speak(self, sound="Warf"):
        return super().speak(sound)
    
class Bulldog(Dog):
    def speak(self, sound="Woooof"):
        return f"{self.name} says: {sound}"

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(buddy)
print(buddy.speak())

print(miles)
print(miles.speak())