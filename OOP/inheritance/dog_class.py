class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def speak(self, sound):
        return f"{self.name} says {sound}"


miles = Dog("Miles", 4, "Jack Russell Terrie")
budy = Dog("Budy", 4, "Dachshund")
jack = Dog("Jack", 4, "Bulldog")
jim = Dog("Jim", 4, "Bulldog")

print(budy.speak("Yap"))
print(jim.speak("Woof"))
print(jack.speak("Wooof"))