# exercise8
print('Exercise 8:\n')

# опитах се да си сортирам листа, без да извикам готовия метод sort(), но ми дава грешка за типа

"""
def sort(arr):
    temporary = 0
    for i in range(len(arr)):
        for j in range(0, len(arr - i ) - 1):
            if arr[j] > arr[j + 1]:
                temporary = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temporary

"""


def biggest_difference(arr):
    # тук се сетих просто да взема най-голямото и най-малкото, без да сортирам
    min = arr[0]
    max = arr[0]
    diff = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]

    diff = min - max
    return diff

print(biggest_difference([4, 2, 7, 3, 1]))
print(biggest_difference([1, 2]))
print(biggest_difference([1, 2, 3, 4, 5]))
print(biggest_difference([-10, -9, -1]))
print(biggest_difference(range(100)))
