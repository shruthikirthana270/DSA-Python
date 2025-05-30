# recursive function to divide the array and merge the sorted parts
def merge(arr, low, high):
    if low >= high:
        return  # base case: single element is already sorted
    mid = (low + high) // 2
    merge(arr, low, mid)       # sort left half
    merge(arr, mid + 1, high)  # sort right half
    sort(arr, low, mid, high)  # merge the two halves

# function to merge two sorted halves
def sort(arr, low, mid, high):
    i = low       # pointer for left half
    j = mid + 1   # pointer for right half
    k = []        # temporary array to store merged result

    # merge elements in sorted order
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            k.append(arr[i])
            i += 1
        else:
            k.append(arr[j])
            j += 1

    # copy remaining elements from left half
    while i <= mid:
        k.append(arr[i])
        i += 1

    # copy remaining elements from right half
    while j <= high:
        k.append(arr[j])
        j += 1

    # copy back the sorted elements to original array
    for ind, val in enumerate(k):
        arr[low + ind] = val

# input: space-separated integers
arr = list(map(int, input().split()))

# calling merge sort
merge(arr, 0, len(arr) - 1)

# output sorted array
print(arr)

# time complexity: O(N log N)
# space complexity: O(N)
