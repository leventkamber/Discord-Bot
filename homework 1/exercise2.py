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