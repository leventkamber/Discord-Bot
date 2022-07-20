# exercise6
print('Exercise 6:\n')


def contains_digits(number, digits):
    current = 0
    counter = 0
    while number != 0:
        current = int(number % 10)
        number = int(number / 10)
        for digit in digits:
            if digit == current:
                counter += 1
    if counter == len(digits):
        return True
    else:
        return False


print(contains_digits(402123, [0, 3, 4]))
print(contains_digits(666, [6, 4]))
print(contains_digits(123456789, [1, 2, 3, 0]))
print(contains_digits(456, []))