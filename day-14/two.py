l = [5,9,4,1,2,8]   # use list instead of tuple
i = 0
j = len(l) - 1

while i <= j:
    l[i], l[j] = l[j], l[i]
    i += 1
    j -= 1

print(l)