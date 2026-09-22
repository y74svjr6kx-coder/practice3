numbers = [5, 2, 8, 1, 3]
result = sorted(numbers)
print(result)


names = ["Anna", "Alexandra", "Tom"]
result = sorted(names, key=lambda x: len(x))
print(result)


students = [
    ("Anna", 20),
    ("Dilnara", 18),
    ("Alex", 19)
]

result = sorted(students, key=lambda x: x[1])
print(result)
