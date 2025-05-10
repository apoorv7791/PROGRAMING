# class and object based programming


class Person:
    def __init__(self):  # Constructor method
        self.name = "John"
        self.age = 36
        self.country = "Norway"

    def display(self):
        print(self.name)
        print(self.age)
        print(self.country)


p1 = Person()  # Creating an object of the Person class
p1.display()  # Calling the display method of the Person class

p2 = Person()  # Creating another object of the Person class
p2.name = "Bob"  # Setting the name attribute of the second object
p2.display()  # Calling the display method of the Person class for the second object
