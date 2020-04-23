class Person:
    def __init__(self, fname, lname, how_old=50):  # notice the default value set for how_old
        self.first = fname
        self.last = lname  # these are properties of the class
        self.age = how_old

    def state_age(self):  # this is a method (or a function that belongs to a class)
        print("I am {} years old.".format(self.age))


class Child(Person):  # this class will inherit the properties and methods of the parent class
    def __init__(self, fname, lname, how_old=50):
        Person.__init__(self, fname, lname, how_old)
        self.mum = "Mummy"
        self.dad = "Daddy"




surname = "Mouse"

dad = Person("Mickey", surname, 31)
mum = Person("Minnie", surname, 32)
rnd = Person("Random", "Random")  # note: didn't state the age, uses the default in the class

print(dad.last)
print(mum.first)
print(rnd.age)

dad.state_age()

dad.age = 100
dad.state_age()


sam = Child("Kid1", surname, 11)
print(sam.mum)
print(sam.dad)
sam.state_age()

bob = Child("Kid2", surname, 11)
print("I am " + bob.first)
print(bob.mum)
print(bob.dad)
bob.state_age()
