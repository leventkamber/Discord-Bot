<<<<<<< HEAD
# exercise 3
print('Exercise 3:')


def to_number(digits):

    num = ""
    for digit in digits:
        num += str(digit)
    return int(num)


print(to_number([1, 2, 3]), to_number([9, 9, 9, 9, 9]), to_number([1, 2, 3, 0, 2, 3]), to_number([21, 2, 33]))
=======
# exercise3
print('Exercise 3:\n')


def is_prime(n):
    for i in range(1, n):
        if (n % i == 0):
            return False
        else:
            return True


print(is_prime(1))
print(is_prime(2))
print(is_prime(8))
print(is_prime(11))
print(is_prime(-10))
>>>>>>> fa81cb9 (Homework 01)
