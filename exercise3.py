# exercise 3
print('Exercise 3:')


def to_number(digits):

    num = ""
    for digit in digits:
        num += str(digit)
    return int(num)


print(to_number([1, 2, 3]), to_number([9, 9, 9, 9, 9]), to_number([1, 2, 3, 0, 2, 3]), to_number([21, 2, 33]))