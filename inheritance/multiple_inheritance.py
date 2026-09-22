class Student:
    def study(self):
        print("I study")

class Worker:
    def work(self):
        print("I work")

class Person(Student, Worker):
    pass

person = Person()
person.study()
person.work()


class Father:
    def father_method(self):
        print("Method from Father")

class Mother:
    def mother_method(self):
        print("Method from Mother")

class Child(Father, Mother):
    pass

child = Child()
child.father_method()
child.mother_method()


class Camera:
    def take_photo(self):
        print("Photo taken")

class Phone:
    def call(self):
        print("Calling...")

class Smartphone(Camera, Phone):
    pass

device = Smartphone()
device.take_photo()
device.call()
