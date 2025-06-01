"""#1st method two sum problem , more time complexity
def twosum(nums,target):
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if(nums[i]+nums[j]==target):
                return i,j
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))
print(twosum(nums, target))                   



==========================================================================
2nd method, two sum problem using dict
def twosum(nums, target):
    d = {}
    for a in range(len(nums)):
        b = target - nums[a]
        if b in d:
            return [d[b], a]
        d[nums[a]] = a
    return []  # if no pair found
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))
print(twosum(nums, target))

============================================================
#3rd method ,array must be sorted in this problem (twosum) ,tow pointer technique
time complexity=0(logn) space complexity=
#it dont work in leetcode because of sorted array,
def twosum(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while(low<high):
        sum=nums[low]+nums[high]
        if (sum==target):
            return "yes"
        elif(sum>target):
            high-=1
        elif(sum<target):
            low+=1
    return "no"
nums=list(map(int,input().split()))
target=int(input())
print(twosum(nums,target))







            




















            

