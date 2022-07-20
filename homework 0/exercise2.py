<<<<<<< HEAD
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
=======
# exercise2
print('Exercise 2:\n')
def sum_of_divisors(n):
    half = n/2
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum+= i
    return sum + n


print(sum_of_divisors(8))
print(sum_of_divisors(7))
print(sum_of_divisors(1))
print(sum_of_divisors(1000))
>>>>>>> fa81cb9 (Homework 01)
