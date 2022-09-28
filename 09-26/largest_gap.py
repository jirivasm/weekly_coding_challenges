
A = [9,4,26,26,0,0,5,20,6,25,5]

def largest_gap(l):
    l = sorted(l)
    result = 0
    temp = 0
    for i in range(len(l)-1):
        temp = l[i+1]-l[i]
        if temp >= result:
            result = temp

    print(result)