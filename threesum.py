# ==================== Three Sum Problem ====================

# Three Sum - Brute Force Method (Time: O(n^3), Space: O(k))

def threeSum(nums):
    t_sum = set()
    n = len(nums)
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    t_sum.add(tuple(temp))
    ans = []
    for triplet in t_sum:
        ans.append(list(triplet))
    return ans

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(threeSum(nums))


# ============================================================

# Three Sum - Optimized using HashMap (Time: O(n^2), Space: O(n))

def threeSum(nums):
    t_sum = set()
    n = len(nums)
    for i in range(0, n - 1):
        hashmap = []
        for j in range(i + 1, n):
            k = -(nums[i] + nums[j])
            if k in hashmap:
                temp = [nums[i], nums[j], k]
                temp.sort()
                t_sum.add(tuple(temp))
            hashmap.append(nums[j])
    ans = []
    for triplet in t_sum:
        ans.append(list(triplet))
    return ans

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(threeSum(nums))
