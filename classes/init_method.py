class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Dilnara")
print(student1.name)


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car1 = Car("Toyota", 2024)
print(car1.brand)
print(car1.year)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Anna", 20)
print(person1.name, person1.age)
