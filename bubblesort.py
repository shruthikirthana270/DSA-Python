# push the maximum element to the last by adjacent swaps
def bubblesort(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]  # swap adjacent if in wrong order
    return arr

arr=[64,25,12,2,11]
print(bubblesort(arr))
