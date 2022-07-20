# exercise5
print('Exercise 5:\n')


def contains_digit(number, digit):
    current = 0
    while number != 0:
        current = int(number % 10)
        number = int(number / 10)
        if current == digit:
            return True
    else:
        return False


print(contains_digit(123, 4))
print(contains_digit(42, 2))
print(contains_digit(100, 0))
print(contains_digit(12346789, 5))