#linear search
l=[8,3,5,7,1,2]
target=5
if target in l:
    print("found element:",l.index(target))       
else:
    print("not found")
# binary search


T = [1,2,3,5,7,8]   # must be sorted
target = 7

low = 0
high = len(T) - 1

while low <= high:
    mid = (low + high) // 2
    
    if T[mid] == target:
        print("Found at index:", mid)
        break
    elif T[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")