list=[1,2,3,4,5]
def maxSubArray(self, nums):
    for start in range(len(list)):
        for end in range(start,len(list)):
            for i in range(start,end+1):
                print(list[i],end="")
            print(" ",end="")
        print()
