def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    pivot = my_list[len(my_list) - 1]
    left = [x for x in my_list if x < pivot]
    right = [x for x in my_list if x > pivot]
    middle = [x for x in my_list if x == pivot]

    return quick_sort(left) + middle + quick_sort(right)

test_list = [18,83,97,89,67,31,27,85,42,89,86,96,39,99,68,22,35]
sorted_list = quick_sort(test_list)
print("Quick sort: ", sorted_list)

def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2
    left = my_list[:mid]
    right = my_list[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

test_list = [18,83,97,89,67,31,27,85,42,89,86,96,39,99,68,22,35]
sorted_list = merge_sort(test_list)
print("Merge sort: ", sorted_list)