numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))


numbers = [2, 5, 7, 10, 3]
result = filter(lambda x: x > 5, numbers)
print(list(result))


ages = [15, 18, 20, 16, 25]
result = filter(lambda age: age >= 18, ages)
print(list(result))
