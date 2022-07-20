# exercise 6
print('Exercise 6:')


def is_decreasing(n):

    if len(n) <= 1:
        return False

    for i in range(1, len(n)):
        if n[i - 1] <= n[i]:
            return False

    return True


print(is_decreasing([5, 4, 3, 2, 1]), is_decreasing([1, 2, 3]), is_decreasing([100, 50, 20]), is_decreasing([1, 1, 1, 1]))