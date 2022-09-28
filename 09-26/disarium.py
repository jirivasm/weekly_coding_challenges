
def is_disarium(number):
    number = str(number)
    result = 0
    for i in range(len(number)):
        result += int(number[i])**(i+1)
    if result == int(number):
        return True
    else:
        return False

print(is_disarium(8))