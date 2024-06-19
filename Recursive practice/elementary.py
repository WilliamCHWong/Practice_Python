def Factorial(number):
    if number == 0:
        return 1
    return number * Factorial(number-1)

def Fibonacci(number):
    if number == 1:
        return 1
    elif number == 2:
        return 1
    return Fibonacci(number - 1) + Fibonacci(number - 2)

def SumDigit(number):
    if number == 0:
        return 0
    return (number % 10) + SumDigit(number // 10)

def Palindrome(string):
    if len(string) == 1:
        return True
    if string[0] != string [-1]:
        return False
    return Palindrome(string[1:-1])

def BinarySearch(list, key):
    low = 0
    high = len(list) - 1
    mid = (high + low) // 2
    if list[mid] == key:
        return mid
    if list[mid] > key:
        return BinarySearch(list[:mid - 1], key)
    else:
        return mid + 1 + BinarySearch(list[mid + 1:], key)
    
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)

def permutation(string, answer=""):
    if len(string) == 0:
        print(answer)
    for i in range(len(string)):
        ch = string[i]
        rest = string[:i] + string[i + 1:]
        permutation(rest, answer + ch)
    
def tower_of_hanoi(n, src, mid, des):
    if n == 1:
        print("Disk {} moves from {} to {}.".format(n, src, des))
        return
    tower_of_hanoi(n - 1, src, des, mid)
    print("Disk {} moves from {} to {}.".format(n, src, des))
    tower_of_hanoi(n - 1, mid, src, des)

def powerfucntion(base, power):
    if power == 0:
        return 1
    elif power > 0:
        return base * powerfucntion(base, power-1)
    else:
        return (1/base) * powerfucntion(base, power+1)

def counteven(mylist):
    if len(mylist) == 0:
        return 0
    i = 0
    if mylist[0]%2 == 0:
        i = 1
    return i + counteven(mylist[1:])

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(counteven(test_list))
