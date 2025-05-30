# Given a sorted array and a target value, find the index of the **lower bound** of the target.

def lowerbound(arr, target):
    n = len(arr)
    low, high = 0, n - 1
    ans = n  # Default answer if no element >= target is found

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid       # Possible lower bound found
            high = mid - 1  # Try to find a smaller index
        else:
            low = mid + 1   # Move to right half

    return ans  # Return the index of the lower bound

# Input: space-separated sorted array and target element
arr = list(map(int, input().split()))
target = int(input())
print(lowerbound(arr, target))
