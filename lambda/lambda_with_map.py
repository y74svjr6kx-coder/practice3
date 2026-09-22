numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))

numbers = [1, 2, 3]
result = map(lambda x: x + 5, numbers)
print(list(result))


names = ["anna", "alex", "dilnara"]
result = map(lambda x: x.upper(), names)
print(list(result))
