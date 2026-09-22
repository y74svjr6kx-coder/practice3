class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()


class Person:
    def hello(self):
        print("Hello!")

class Student(Person):
    pass

student = Student()
student.hello()


class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    pass

car = Car()
car.move()
