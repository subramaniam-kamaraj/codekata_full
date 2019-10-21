'''Create a Pets class that holds instances of dogs; this class is completely separate
from the Dog class. In other words, the Dog class does not inherit from
the Pets class. Then assign three dog instances to an instance of the Pets class.
Start with the following code below. Your output should look like this:
I have 3 dogs.
Tom is 6.
Fletcher is 7.
Larry is 9.
And they're all mammals, of course. '''

                                                    # Parent class
class Dog:
                                                    # Class attribute
    species = 'mammal'
                                                    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
                                                    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
                                                    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
                                                    # Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
                                                    # Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class pet(Dog):
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


dogs_collection = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

                                                # Instantiate the Pets class
my_pets = pet(dogs_collection)

                                                # Output
print("I have {} dogs.".format(len(dogs_collection)))
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))

