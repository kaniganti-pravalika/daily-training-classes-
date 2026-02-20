n = int(input("Enter n value: "))
nums = list(map(int, input().split()))

for i in range(n):
    if nums[i] != -1:
        count = 1
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                count += 1
                nums[j] = -1
        print(nums[i], "--->", count)
#using dictonary
n=int(input())
dict={}
for i in range(n):
    nums=int(input("enter nums:"))
    if nums in dict:
        dict[nums]+=1
    else:
        dict[nums]=1
print(dict)

name=input()
freq=()
for ch in name:
    if name in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)
for key in freq:
    print(key,"-->",freq[key])

    
