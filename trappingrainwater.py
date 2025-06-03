def trap(height):
    n = len(height)
    leftmax = [-1] * n
    leftmax[0] = height[0]
    for i in range(1, n):
        leftmax[i] = max(height[i], leftmax[i - 1])  
    rightmax = [-1] * n  
    rightmax[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        rightmax[i] = max(height[i], rightmax[i + 1])
    minarray = []
    for i in range(0, n):
        minarray.append(min(rightmax[i], leftmax[i]))  
    result = 0
    for i in range(0, n):
        result += minarray[i] - height[i]
    return result
# Input
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output
print("Trapped water:", trap(height))

    
