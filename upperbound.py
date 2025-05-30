# Given a sorted array and a target value, find the index of the **upper bound** of the target.
def upperbound(arr, target):
    n = len(arr)
    low, high = 0, n - 1
    ans = n  # Default answer if no element > target is found

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ans = mid       # Possible upper bound found
            high = mid - 1  # Try to find smaller index
        else:
            low = mid + 1   # Move to right half

    return ans  # Return index of upper bound

arr = list(map(int, input().split()))
target = int(input())
print(upperbound(arr, target))
