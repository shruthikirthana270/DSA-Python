def findpages(arr, n, m):
    def canweallocate(maxpages, arr):
        noofpages_alloc= arr[0]
        students = 1
        for pages in range(1, len(arr)):
            if arr[pages] + noofpages_alloc<= maxpages:
                noofpages_alloc+= arr[pages]
            else:
                noofpages_alloc = arr[pages]
                students += 1
        return students
    if m > len(arr):
        return -1
    low = max(arr)
    high = sum(arr)
    while(low<=high):
        maxpages=(low+high)//2
        if canweallocate(maxpages, arr) <= m:
            high=maxpages-1
        else:
            low=maxpages+1
    return low
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
print(findpages(arr, n, m))
