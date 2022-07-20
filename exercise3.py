# exercise 3
def nan_expand(num):
    res = ""

    for i in range(0, num):
        res += "Not a "
    if num > 0:
        res += "NaN"
    return res


print(nan_expand(0))
print(nan_expand(1))
print(nan_expand(2))
print(nan_expand(3))