<<<<<<< HEAD
# exercise 1
print('Exercise 1:')


def sum_of_digits(n):

    total = 0
    while n != 0:
        total += int(abs(n) % 10)
        n = int(n/10)
    return total


print(sum_of_digits(1325132435356), sum_of_digits(123), sum_of_digits(6), sum_of_digits(-10))
=======
# exercise1
print('Exercise 1:')


def sum_of_min_and_max(arr):
    sum = 0
    arr.sort()
    if len(arr) == 0:
        return 0

    sum = arr[0] + arr[-1]
    return sum


print(sum_of_min_and_max([1, 2, 3, 4, 5, 6, 8, 9]))
print(sum_of_min_and_max([-10, 5, 10, 100]))
print(sum_of_min_and_max([1]))
print(sum_of_min_and_max([3, 4, 1, 2]))
>>>>>>> fa81cb9 (Homework 01)
