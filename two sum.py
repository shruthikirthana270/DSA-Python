# ==================== Two Sum Problem ====================

# 1st method: Brute Force approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Approach: Check every pair to find the one that sums to target
def twosum(nums, target):
    n = len(nums)
    for i in range(0, n):
        for j in range(i + 1, n):
            if(nums[i] + nums[j] == target):
                return i, j

nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))
print(twosum(nums, target))


# =============================================================

# 2nd method: Using Dictionary (HashMap)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Store elements in a dictionary and check if complement exists
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


# ============================================================

# 3rd method: Two Pointer Technique
# Prerequisite: Array must be sorted
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Note: Will not work on LeetCode unless input is sorted
def twosum(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while(low < high):
        sum = nums[low] + nums[high]
        if(sum == target):
            return "yes"
        elif(sum > target):
            high -= 1
        elif(sum < target):
            low += 1
    return "no"

nums = list(map(int, input().split()))
target = int(input())
print(twosum(nums, target))

