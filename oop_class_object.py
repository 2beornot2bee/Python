## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

## ?? Dog is-a Animal and came from animal class / related to each other by a class relationship

class Dog(Animal):

    def __init__(self,name):
        ##Dog class has a __init__ that takes self and name parameters
        self.name=name


##Cat is-a Animal and came from animal class 

class Cat(Animal):

    def __init__(self,name):
        ##Cat class has a __init__ that takes self and name parameters
        self.name=name


##Person is-a object as well as class. 

class Person(object):

    def __init__(self,name):
        ## Person class has-a __init__ that takes self and name parameters

        ##Person has-a pet of some kind
        self.pet=None



##Employee is-a person ....

class Employee(Person):
    def __init__(self,name,salary):
        ##?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ##?? Employee has-a __init__ that takes self,name and salary parameters
        self.salary=salary

##Fish is-a object

class Fish(object):
    pass

##Salmon is a fish

class Salmon(Fish):
    pass
##Halibu is-a fish
class Halibut(Fish):
    pass

##rover is-a dog
rover=Dog("Rover")

##satan is-a cat, it is instance of Cat.
satan=Cat("Satan")
##marry is-a Person, she is instance of person.
mary=Person("Mary")
##marry has a per nanes satan
mary.pet=satan
##frank is an employee and she is instance of employee
frank=Employee("Frank",120000)
##frank has pet names rover
frank.pet=rover
##flipper is a fish and it is a instance of fish
flipper=Fish()
##crouse is a salmon and it is an instance of salmon
crouse=Salmon()
##harry is a halibut and it is an instance of Halibuıt.
harry=Halibut()





        
