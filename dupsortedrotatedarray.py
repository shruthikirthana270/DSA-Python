# search key in a rotated sorted array with duplicates
def dubsortedroratedarray(arr,key):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2

        if arr[mid]==key:
            return True  # key found

        # if duplicates at boundaries
        if arr[low]==arr[mid]==arr[high]:
            low+=1
            high-=1

        # left half is sorted
        elif arr[low]<=arr[mid]:
            if arr[low]<=key<=arr[mid]:
                high=mid-1  # key lies in left
            else:
                low=mid+1   # key lies in right

        # right half is sorted
        else:
            if arr[mid]<=key<=arr[high]:
                low=mid+1   # key lies in right
            else:
                high=mid-1  # key lies in left

    return False  # key not found

arr=list(map(int,input().split()))
key=int(input())
print(dubsortedroratedarray(arr,key))
