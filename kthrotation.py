
# Given a rotated sorted array, find the index of the minimum element.
# This index represents the number of times the sorted array has been rotated (k-th rotation).
def kthrotation(arr):
    n = len(arr)
    low, high = 0, n - 1
    Min = float("inf")       # Initialize minimum value
    mIndex = -1              # Index of the minimum element

    while low <= high:
        mid = (low + high) // 2

        # If subarray is already sorted
        if arr[low] <= arr[high]:
            if arr[low] < Min:
                Min = arr[low]
                mIndex = low
            break  # Array is sorted, so no more rotation to check

        # If left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] < Min:
                Min = arr[low]
                mIndex = low
            low = mid + 1

        # If right half is sorted
        else:
            if arr[mid] < Min:
                Min = arr[mid]
                mIndex = mid
            high = mid - 1

    return mIndex  # Return index of the minimum element
arr = list(map(int, input().split()))
print(kthrotation(arr))
