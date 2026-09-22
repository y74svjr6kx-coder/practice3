class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

student = Student("Dilnara")
print(student.name)


class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Woof!")

dog = Dog()
dog.sound()


class Person:
    def hello(self):
        print("Hello!")

class Student(Person):
    def hello(self):
        super().hello()
        print("I am a student")

student = Student()
student.hello()
