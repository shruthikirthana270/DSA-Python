# select minimum element and swap
def selection_sort(arr):
    n=len(arr)
    for i in range(0,n):
        min=i  # assume current index is min
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j  # update min index
        arr[i],arr[min]=arr[min],arr[i]  # swap
    return arr

arr=[64,25,12,22,11]
print(selection_sort(arr))
