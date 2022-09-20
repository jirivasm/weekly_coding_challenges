# Problem Statement
# Write a program that accepts sets of three numbers and prints the
# second-maximum number among the three.
a =[1, 2, 3]
b = [10, 15, 5]
c = [100, 999, 500]

def find_middle_number(lists):
    list = sorted(lists)
    return list[1]

print (find_middle_number(a))
print (find_middle_number(b))
print (find_middle_number(c))





