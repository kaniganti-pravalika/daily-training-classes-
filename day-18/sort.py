l = [9, 8, 1, 5, 4, 7]

# Selection sort
for i in range(len(l)):
    min_idx = i
    for j in range(i + 1, len(l)):
        if l[j] < l[min_idx]:
            min_idx = j
    l[i], l[min_idx] = l[min_idx], l[i]

print(l)

#sorted square
def sortedsquare(nums):
    left,right=0,len(nums)-1
    result=[0]*len(nums)
    pos=len(nums)-1
    while left<=right:
        if abs(nums[left])>abs(nums[right]):
            result[pos]=nums[left]**2
            left+=1
        else:
            result[pos]=nums[right]**2
            right-=1
        pos-=1
    return result 

