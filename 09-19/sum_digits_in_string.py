


phrase = 'asdasd1231asd'


def is_digit(text):
    result = 0
    for i in text:
        if i.isdigit():
            result += int(i)
    return result
    
print(is_digit(phrase))


