import re
def is_digit(char):
    nums_in_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if char in nums_in_char:
        return True
    else:
        return False



#първоначално тръгнах по този начин да проверявам символ по символ дали е число
#обаче осъзнах че така взимам не цялото число, а само 1 цифра от него
"""
def sum_of_numbers(st):

    sum_of_nums = 0
    for i in range(0, len(st)):
        if is_digit(st[i]):
            sum_of_nums += int(st[i])
    return sum_of_nums


print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
"""

#след това прочетох за регулярни изрази от 'w3schools' и видях че има по лесен начин
def sum_of_numbers(st):
    sum = 0
    list_of_nums = re.findall(r'\d+', st)
    for num in list_of_nums:
        sum += int(num)
    return sum

print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))