def quicksort(arr):
    # function to place pivot in correct position
    def partition(arr,low,high):
        pivot=arr[low]  # choose first element as pivot
        i=low+1
        j=high
        while i<j:
            while i<high and arr[i]<=pivot:
                i+=1
            while j>low and arr[j]>=pivot:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]  # swap
        arr[low],arr[j]=arr[j],arr[low]  # place pivot at right position
        return j  # return pivot index

    # recursive function to sort array
    def qs(arr,low,high):
        if low<high:
            pIndex=partition(arr,low,high)  # get pivot index
            qs(arr,low,pIndex-1)  # sort left part
            qs(arr,pIndex+1,high)  # sort right part

    qs(arr,0,len(arr)-1)  # initial call
    return arr  # return sorted array

arr=list(map(int,input().split()))  # take input
print(quicksort(arr))  # print sorted array
