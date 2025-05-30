def binarysearch(arr,target):
    n=len(arr)
    low=0
    high=n-1
    while(low<=high):#array is sorted
        mid=(low+high)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):#example arr[mid]=23 < target=35  ->  (23<35)
            low=mid+1 #eliminate left search space
        elif(arr[mid]>target):#example arr[mid]=40 > target=35 ->(40>35)
            high=mid-1#eliminate right search space
    return -1
arr=[1,2,3,4,5,6,7]
target=2
print(binarysearch(arr,target))
