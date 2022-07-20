#exercise 1
def is_anagram(fst_word, snd_word):
    res = True
    fst_word.lower()
    snd_word.lower()
    first = sorted(fst_word)
    second = sorted(snd_word)
    if(first == second):
        res = True
    return res


print(is_anagram("BRADE", "BeaRD"))
print(is_anagram("TOP_CODER", "COTO_PRODE"))