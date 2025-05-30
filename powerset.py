def generate(ind, curr, ans, nums):
    if ind == len(nums):
        ans.append(curr.copy())  # Add the current subset to the answer list
        return
    # Include nums[ind] in the current subset
    curr.append(nums[ind])
    generate(ind + 1, curr, ans, nums)
    # Exclude nums[ind] from the current subset (backtrack)
    curr.pop()
    generate(ind + 1, curr, ans, nums)

def subset(nums):
    ind = 0            # Start index
    curr = []          # Current subset
    ans = []           # All subsets collected here
    generate(ind, curr, ans, nums)
    return ans
nums=list(map(int,input().split()))
print(subset(nums))





















