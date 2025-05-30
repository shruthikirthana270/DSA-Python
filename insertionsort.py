# insert elements into their correct position by shifting
def insertionsort(arr):
    n=len(arr)
    for i in range(0,n):
        while i>0 and arr[i-1]>arr[i]:
            arr[i-1],arr[i]=arr[i],arr[i-1]  # swap if left is greater
            i-=1  # move left
    return arr

arr=[3,5,7,9,1,2]
print(insertionsort(arr))
