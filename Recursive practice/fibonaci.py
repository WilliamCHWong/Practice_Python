def fibonacci(number):
    if number == 1:
        return 1
    if number == 2:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

for i in range(1, 21):
    print(i, fibonacci(i))