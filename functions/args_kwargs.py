def numbers(*args):
    print(args)
numbers(1, 2, 3, 4)

def students(*names):
    for name in names:
        print(name)
students("Anna", "Dilnara", "Alex")

def student(**info):
    print(info)
student(name="Dilnara", age=18, city="Almaty")
