# Given a **rotated sorted array**, search for a given key and return its index.
# If the key is not present, return -1.
# The array contains **distinct integers**.
def search(arr, key):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        # If key is found
        if arr[mid] == key:
            return mid

        # Check if the left half is sorted
        elif arr[low] <= arr[mid]:
            # If key lies in the left half
            if arr[low] <= key <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Else the right half must be sorted
        else:
            # If key lies in the right half
            if arr[mid] <= key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1  # Key not found

# Input from user
arr = list(map(int, input("Enter array elements (rotated sorted): ").split()))
key = int(input("Enter key to search: "))
print(search(arr, key))
