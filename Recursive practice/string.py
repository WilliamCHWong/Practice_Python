def reverse_string(s):
    if len(s) == 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("qwertyuiop"))

def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return (True and is_palindrome(s[1:-1]))

print(is_palindrome("mappam"))
print(is_palindrome("apple"))
