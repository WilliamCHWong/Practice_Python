def two_sum(numbers, target):
    store = {}
    for index, num in enumerate(numbers):
        diff = target - num
        if diff in store:
            return [store[diff], index]
        store[num] = index
    return []

test_num = [2, 7, 11, 15, 32, 9]
target = 16
print(two_sum(test_num, target))
