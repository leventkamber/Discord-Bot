# exercise 2
print('Exercise 2:')


def to_digits(n):

    num = 0
    my_list = []
    while n != 0:
        num = int(abs(n) % 10)
        n = int(n/10)
        my_list.append(num)
    my_list.reverse()
    return my_list


print(to_digits(123), to_digits(99999), to_digits(123023))