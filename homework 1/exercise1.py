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