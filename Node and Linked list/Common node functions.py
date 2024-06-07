class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
def print_list(head):
    print(head.data)
    if head.next:
        print_list(head.next)
    
def print_even(head):
    if head.data % 2 == 0:
        print(head.data)
    if head.next:
        print_even(head.next)

def insert_after(head, value, data):
    new = Node(data)
    current = head
    while current.data != value and current.next:
        current = current.next
    new.next = current.next
    current.next = new

def check(head):
    list = []
    current = head
    while current.next:
        list.append(current)
        current = current.next
    list.append(current)
    length = len(list)
    for i in range(0, length):
        if list[i].data != list[length - i - 1].data:
            return False
    return True

def is_palindrome(head):
    current = head
    stack = []
    while current is not None:
        stack.append(current.data)
        current = current.next
    current = head
    while current is not None:
        if(current.data != stack.pop()):
            return False
        current = current.next
    return True

head = Node(2)
head.next = Node(3)
head.next.next = Node(3)
head.next.next.next = Node(2)

print(check(head))
