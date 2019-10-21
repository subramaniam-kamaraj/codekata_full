'''
Exercise 1:” The oldest dog”
Using the Dog class described below, instantiate three new dogs, each with a
different age. Then write a function called, get_biggest_number(), that takes any
number of ages (*args) and returns the oldest one. Then output the age of the
oldest dog like so:
The oldest dog is 7 years old.   '''


class Dog:                      # Class Attribute
    species = 'mammal'

                                # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
                                #function calc for maximum of given ages in the arguments
    def get_biggest_number(age1,age2,age3):
        print("The oldest dog is {} years old".format(max(age1,age2,age3)))
                                #object creating with constructor invoking
Dog1=Dog('jimmy',10)
Dog2=Dog('julley',6)
Dog3=Dog('ceaser',12)
Dog.get_biggest_number(Dog1.age,Dog2.age,Dog3.age)      #finally method calling
