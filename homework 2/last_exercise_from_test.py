dic_of_romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_integer(roman_num):
    result = 0
    shouldSkip = False
    for i in range(len(roman_num)):
        if shouldSkip:
            shouldSkip = False
            continue
        if i + 1 < len(roman_num):
            if roman_num[i] == "I":
                if roman_num[i + 1] == "X" or roman_num[i + 1] == "V":
                    result += dic_of_romans[roman_num[i + 1]] - dic_of_romans[roman_num[i]]
                    shouldSkip = True
            elif roman_num[i] == "X":
                if roman_num[i + 1] == "L" or roman_num[i + 1] == "C":
                    result += int(dic_of_romans[roman_num[i + 1]]) - dic_of_romans[roman_num[i]]
                    shouldSkip = True
            elif roman_num[i] == "C":
                if roman_num[i + 1] == "D" or roman_num[i + 1] == "M":
                    result += int(dic_of_romans[roman_num[i + 1]]) - dic_of_romans[roman_num[i]]
                    shouldSkip = True
        if shouldSkip:
            continue
        result += int(dic_of_romans[roman_num[i]])
    return result


print(roman_to_integer("III"))
print(roman_to_integer("IXI"))
print(roman_to_integer("LVIII"))
print(roman_to_integer("MCMXCIV"))
