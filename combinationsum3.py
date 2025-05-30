def generate(curr,ans,k,n):#fun def
    if n==0 and len(curr)==k:
        ans.append(curr.copy())  # found valid combination
        return
    if n<0:
        return  # if sum exceeds n, stop
    if n==0 and len(curr)<k:
        return  # sum is fine but size is less
    if len(curr)>k:
        return  # too many elements

    # decide starting element
    if len(curr)==0:
        ele=1
    else:
        ele=curr[-1]+1  # next number must be greater

    # try numbers from ele to 9
    for i in range(ele,10):
        curr.append(i)  # add current number
        generate(curr,ans,k,n-i)  # recur with reduced target
        curr.pop()  # backtrack

# main function
def combinationsum3(k,n):
    curr=[]
    ans=[]
    generate(curr,ans,k,n)#fun call
    return ans

# input
k=int(input())
n=int(input())
print(combinationsum3(k,n))
