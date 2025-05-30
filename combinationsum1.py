def generate(ind,curr,ans,candidates,target):
    if(target==0):  #base case:1 it means we found correct combination
        ans.append(curr.copy())
        return
    if(target<0): #base case:2 it means no more numbers left to check
        return
    if(ind==len(candidates)):
       return
    curr.append(candidates[ind])
    generate(ind,curr,ans,candidates,target-candidates[ind])
    curr.pop() 
    generate(ind+1,curr,ans,candidates,target)
def combinationsum(candidates,target):#main function
    ind=0
    curr=[]
    ans=[]
    generate(ind,curr,ans,candidates,target)
    return ans
candidates=list(map(int,input().split()))
target=int(input())
print(combinationsum(candidates,target))
