class person:
    "Employee details"
    #def __init__(self):
    #    self.name=None
    #    self.occupation=None
    def details(abc,name,occupation):
        abc.name=name
        abc.occupation=occupation
        print("name: ",name)
        print("occupation: ",occupation)
p1=person()
print(person.__doc__)
#print(person.a)
p1.details('vijay','Full Stack Developer')
#print(p1.name)
#print(p1.occupation)