'''In the above program, add an instance attribute of is_hungry = True to
the Dog class. Then add a method called eat() which changes the value
of is_hungry to False when called. Figure out the best way to feed each dog and
then output “My dogs are hungry.” if all are hungry or “My dogs are not hungry.”
if all are not hungry. The final output should look like this:
I have 3 dogs.
Tom is 6.
Fletcher is 7.
Larry is 9.
And they're all mammals, of course.
My dogs are not hungry. '''


class Dog:
    species="mammal"
                                # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
                                 # instance method
    def eat(self):
        self.is_hungry=False

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


# Create instances of dogs
dogs_collection = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

                                # Instantiate the Pets class
my_pets = Pets(dogs_collection)

                                        # Output
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    dog.eat()
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}, of course.".format(dog.species))

are_my_dogs_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True

if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")# Create instances of dogs
