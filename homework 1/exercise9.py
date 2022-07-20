# exercise9
print('Exercise 9:\n')


def slope_style_score(scores):
    current_score = 0
    final_score = 0

    max = scores[0]
    min = scores[0]
    for i in range(len(scores)):
        if scores[i] < min:
            min = scores[i]
        elif scores[i] > max:
            max = scores[i]
    scores.remove(min)
    scores.remove(max)

    for score in scores:
        current_score += score
    final_score = current_score / len(scores)
    return round(final_score, 2)


print(slope_style_score([94, 95, 95, 95, 90]))
print(slope_style_score([60, 70, 80, 90, 100]))
print(slope_style_score([96, 95.5, 93, 89, 92]))