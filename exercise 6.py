def my_func(some_list, num):
    pairs = []
    for i in range(0, len(some_list)):
        for j in range(i + 1, len(some_list)):
            if (some_list[i] + some_list[j]) == num:
                pairs.append([some_list[i], some_list[j]])

    return pairs


print(my_func([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(my_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 16, 17], 20))
print(my_func([9, 8, 7, 6, 5, 4, 3, 2, 1], 8))



def func(some_list, num):
    pairs = []
    for i in range(0, len(some_list) // 2 ):
        for j in range(0, len(some_list)):
            if (some_list[i] + some_list[j]) == num:
                pairs.append([some_list[i], some_list[j]])

    return pairs


print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 16, 17], 20))
print(func([9, 8, 7, 6, 5, 4, 3, 2, 1], 8))
