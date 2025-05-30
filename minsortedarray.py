# Given a rotated sorted array (with no duplicates), find the **minimum element** in the array.
def minsortedarray(arr):
    n = len(arr)
    low, high = 0, n - 1
    Min = float("inf")  # Initialize minimum value as infinity

    while low <= high:
        mid = (low + high) // 2

        # If the subarray is already sorted
        if arr[low] <= arr[high]:
            Min = min(Min, arr[low])
            break  # No need to continue, this is the minimum part

        # If left part is sorted
        if arr[low] <= arr[mid]:
            Min = min(Min, arr[low])
            low = mid + 1  # Move to right half

        # If right part is sorted
        else:
            Min = min(Min, arr[mid])
            high = mid - 1  # Move to left half

    return Min  # Return the minimum element

#  Input: space-separated rotated sorted array
arr = list(map(int, input().split()))
print(minsortedarray(arr))
