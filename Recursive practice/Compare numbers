def get_max(numbers):
    current = numbers[0]
    if len(numbers) == 1:
        return current
    sub = get_max(numbers[1:])
    return current if current > sub else sub

print(get_max([2, 1, 5, 3, 4]))
