# exercise4
print('Exercise 4:\n')


def is_int_palindrome(n):
    current = n
    changed = 0
    while (n > 0):
        changed = changed * 10 + (n % 10)
        n //= 10
    if (current == changed):
        return True
    else:
        return False


print(is_int_palindrome(1))
print(is_int_palindrome(42))
print(is_int_palindrome(100001))
print(is_int_palindrome(999))
print(is_int_palindrome(123))