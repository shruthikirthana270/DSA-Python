def floorandceil(a,n,x):
    # Function to find the floor (largest element <= x)
    def getfloor(a,n,x):
        low,high,ans=0,n-1,-1
        while low<=high:
            mid=(low+high)//2
            if a[mid]<=x:
                ans=a[mid]     # Store potential floor
                low=mid+1      # Move to right half
            else:
                high=mid-1     # Move to left half
        return ans

    # Function to find the ceil (smallest element >= x)
    def getceil(a,n,x):
        low,high,ans=0,n-1,-1
        while low<=high:
            mid=(low+high)//2
            if a[mid]>=x:
                ans=a[mid]     # Store potential ceil
                high=mid-1     # Move to left half
            else:
                low=mid+1      # Move to right half
        return ans

    floor=getfloor(a,n,x)      # Get floor of x
    ceil=getceil(a,n,x)        # Get ceil of x
    return (floor,ceil)        # Return as a tuple

a=list(map(int,input().split()))  # Input list elements
n=len(a)                          # Length of list
x=int(input())                    # Input value to find floor and ceil
print(floorandceil(a,n,x))        
