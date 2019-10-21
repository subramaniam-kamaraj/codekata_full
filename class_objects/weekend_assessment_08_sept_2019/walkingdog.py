'''Next, add a walk() method to both the Pets and Dog classes so that when you
call the method on the Pets class, each dog instance assigned to the Pets class
will walk(). Save this as dog_walking.py. This is slightly more difficult.
Start by implementing the method in the same manner as the speak() method.
As for the method in the Pets class, you will need to iterate through the list of
dogs, then call the method itself.
The output should look like this:
Tom is walking!
Fletcher is walking!
Larry is walking!'''


class Dog:
    species="mammal"
    is_hungry = True
                                # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
                                 # instance method
    def eat(self):
        self.is_hungry=False

    def walk(self):
        return "{} is walking".format(self.name)

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

class Pets:
    dogs = []
    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())


# Create instances of dogs
dogs_collection = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

                                # Instantiate the Pets class
my_pets = Pets(dogs_collection)

my_pets.walk()                                   # Outpu