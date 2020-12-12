def func(string,key):
    lenght = len(string)
    result = ""
    last = False
    for i in range(0, lenght):
        if string[i].isalpha():
            number = ord(string[i])
            if number == 122 or number == 90:
                number = number - 26
            elif number == 1071 or number == 1103:
                number = number - 32
            elif number == 32:
                number = number - 1
            result = result + chr(number + key)
        elif string[i].isdigit():
            if i < lenght - 1:
                if string[i + 1].isdigit():
                    result = result + string[i]
                    last = True
                else:
                    number = ord(string[i])
                    if number == 57:
                        number = number - 10
                    result = result + chr(number + key)
            elif (last == True) and (i >= lenght - 1):
                number = ord(string[i])
                if number == 57:
                    number = number - 10
                result = result + chr(number + key)
        else:
            result = result + string[i]
    return result
