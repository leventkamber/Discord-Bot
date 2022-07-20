# exercise 4
print('Exercise 4:')


def fib_number(n):

    first = 0
    second = 1
    result = ''
    for num in range(1, n+1):
        if num <= 1:
            next_num = num
        else:
            next_num = first + second
            first = second
            second = next_num

        result += str(next_num)
    return result


print(fib_number(3), fib_number(10), fib_number(9), fib_number(5))