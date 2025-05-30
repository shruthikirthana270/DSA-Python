# function to generate combinations that sum up to target
def generate(ind,curr,ans,candidates,target):
    if target==0:
        ans.append(curr.copy())  # found a valid combination
        return
    if target<0:
        return  # if target goes below 0, stop
    if ind==len(candidates):
        return  # if reached end of list, stop

    curr.append(candidates[ind])  # take current number
    generate(ind+1,curr,ans,candidates,target-candidates[ind])  # move to next index with reduced target
    curr.pop()  # backtrack and remove the last added number

    # skip duplicates
    for i in range(ind+1,len(candidates)):
        if candidates[i]!=candidates[ind]:  # check if next number is different
            generate(i,curr,ans,candidates,target)
            break

# main function to start the process
def combination2(candidates,target):
    candidates.sort()  # sort to handle duplicates easily
    ind=0
    ans=[]  # final answer list
    curr=[]  # to store current combination
    generate(ind,curr,ans,candidates,target)
    return ans

candidates=[1,2,2,2,3]
target=int(input())  # take input from user
print(combination2(candidates,target))  # print the result
