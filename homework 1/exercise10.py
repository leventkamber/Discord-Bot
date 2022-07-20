# exercise10
print('Exercise 10:\n')
#тук се опитах да я направя с вложен switch без да ползвам изобщо if/else, обаче не знам как да проверя за деня без изобщо да ползвам if/else
"""
def what_is_my_sign(day, month):
    sign = ''
    match month:
        case 1:
            match day:
                case range(1,20):
                    sign = 'Capricorn'
                case range(21,31):
                    sign = 'Aquarius'
        case 2:
            match day:
                case range(1,19):
                    sign = 'Aquarius'
                case range(20,29):
                    sign = 'Pisces'      
        case 3:
            match day:
                case range(1,21):
                    sign = 'Pisces'
                case range(22,31):
                    sign = 'Aries'     
        case 4:
            match day:
                case range(1,20):
                    sign = 'Aries'
                case range(21,30):
                    sign = 'Taurus'   
        case 5:
            match day:
                case range(1,21):
                    sign = 'Taurus'
                case range(22,31):
                    sign = 'Gemini' 
        case 6:
            match day:
                case range(1,21):
                    sign = 'Gemini'
                case range(22,30):
                    sign = 'Cancer'    
        case 7:
            match day:
                case range(1,23):
                    sign = 'Cancer'
                case range(24,31):
                    sign = 'Leo' 
        case 8:
            match day:
                case range(1,23):
                    sign = 'Leo'
                case range(24,31):
                    sign = 'Virgo' 
        case 9:
            match day:
                case range(1,23):
                    sign = 'Virgo'
                case range(24,30):
                    sign = 'Libra'  
        case 10:
            match day:
                case range(1,23):
                    sign = 'Libra'
                case range(24,31):
                    sign = 'Scorpio'    
        case 11:
            match day:
                case range(1,22):
                    sign = 'Scorpio'
                case range(23,30):
                    sign = 'Sagittarius'  
        case 12:
            match day:
                case range(1,22):
                    sign = 'Sagittarius'
                case range(23,31):
                    sign = 'Capricorn'   

    return sign
"""


def what_is_my_sign(day, month):
    sign = ''
    match month:
        case 1:
            if day < 20:
                sign = 'Capricorn'
            else:
                sign = 'Aquarius'
        case 2:
            if day < 19:
                sign = 'Aquarius'
            else:
                sign = 'Pisces'
        case 3:
            if day < 21:
                sign = 'Pisces'
            else:
                sign = 'Aries'
        case 4:
            if day < 20:
                sign = 'Aries'
            else:
                sign = 'Taurus'
        case 5:
            if day < 21:
                sign = 'Taurus'
            else:
                sign = 'Gemini'
        case 6:
            if day < 21:
                sign = 'Gemini'
            else:
                sign = 'Cancer'
        case 7:
            if day < 23:
                sign = 'Cancer'
            else:
                sign = 'Leo'
        case 8:
            if day < 23:
                sign = 'Leo'
            else:
                sign = 'Virgo'
        case 9:
            if day < 23:
                sign = 'Virgo'
            else:
                sign = 'Libra'
        case 10:
            if day < 23:
                sign = 'Libra'
            else:
                sign = 'Scorpio'
        case 11:
            if day < 22:
                sign = 'Scorpio'
            else:
                sign = 'Sagittarius'
        case 12:
            if day < 22:
                sign = 'Sagittarius'
            else:
                sign = 'Capricorn'

    return sign


print(what_is_my_sign(5, 8))
print(what_is_my_sign(29, 1))
print(what_is_my_sign(30, 6))
print(what_is_my_sign(31, 5))
print(what_is_my_sign(2, 2))
print(what_is_my_sign(8, 5))
print(what_is_my_sign(9, 1))