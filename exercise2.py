
#exercise 2


def count_words(arr):
    words_dict = {}
    for w in arr:
        if w not in words_dict:
            words_dict[w] = 1
        else:
            words_dict[w] +=1
    return words_dict


print(count_words(["apple", "banana", "apple", "pie"]))