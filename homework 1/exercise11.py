# exercise11
print('Exercise 11:\n')


def calculate_coins(sum):
    c1, c2, c5, c10, c20, c50, c100 = 0, 0, 0, 0, 0, 0, 0
    coins = [100, 50, 20, 10, 5, 2, 1]
    result = {}
    sum *= 100

    while (sum > 0):
        if sum >= coins[0]:
            sum -= coins[0]
            c100 += 1
        elif sum < coins[0] and sum >= coins[1]:
            sum -= coins[1]
            c50 += 1
        elif sum < coins[1] and sum >= coins[2]:
            sum -= coins[2]
            c20 += 1
        elif sum < coins[2] and sum >= coins[3]:
            sum -= coins[3]
            c10 += 1
        elif sum < coins[3] and sum >= coins[4]:
            sum -= coins[4]
            c5 += 1
        elif sum < coins[4] and sum >= coins[5]:
            sum -= coins[5]
            c2 += 1
        else:
            c1 += 1
            sum -= coins[-1]

    result.update({
        '1': c1,
        '2': c2,
        '5': c5,
        '10': c10,
        '20': c20,
        '50': c50,
        '100': c100
    })
    return result


print(calculate_coins(0.53))
print(calculate_coins(8.94))
print(calculate_coins(4.34))