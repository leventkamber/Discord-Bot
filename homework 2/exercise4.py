# exercise 4
def group(arr):
    groups = []
    inner_group = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            inner_group.append(arr[i-1])
        else:
            groups.append(inner_group)
            inner_group = []
            inner_group.append(arr[i])
    groups.append(inner_group)

    return groups


print(group([1, 1, 1, 2, 3, 1, 1]))
print(group([1, 2, 1, 2, 3, 3]))

def max_consecutive(items):
    list_of_items = group(items)
    max = -12312312312312
    for item in list_of_items:
            if len(item) > max:
                max = len(item)
    return max


print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))

print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))