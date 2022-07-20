# exercise 5
print('Exercise 5:')


def is_number_balanced(n):

    left_side = 0
    right_side = 0
    if n in range(0, 9):
        return True
    for i in range(0, int(len(n) // 2)):
        left_side = left_side + int(n[i])
        right_side = (right_side + int(n[len(n) - 1 - i]))
    if left_side == right_side:
        return True
    else:
        return False


print(is_number_balanced(str(9)), is_number_balanced(str(4518)), is_number_balanced(str(28471)), is_number_balanced(str(1238033)))