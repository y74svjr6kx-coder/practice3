class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

dog = Dog()
dog.sound()


class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    def introduce(self):
        print("I am a student")

student = Student()
student.introduce()


class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def move(self):
        print("Car drives")

car = Car()
car.move()
