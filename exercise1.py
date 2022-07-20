# exercise 1
print('Exercise 1:')


def sum_of_digits(n):

    total = 0
    while n != 0:
        total += int(abs(n) % 10)
        n = int(n/10)
    return total


print(sum_of_digits(1325132435356), sum_of_digits(123), sum_of_digits(6), sum_of_digits(-10))