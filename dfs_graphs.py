def depthfirstsearch(node,visited,adj,ans):
    visited[node]=1
    ans.append(node)
    for i in adj[node]:
        if(visited[i]==0):
            depthfirstsearch(i,visited,adj,ans)
def dfs(adj):
    v=len(adj)
    visited=[0]*v
    ans=[]
    node=0
    if(visited[node]==0):
        depthfirstsearch(node,visited,adj,ans)
    return ans
adj_list = [[1, 2],[0, 3],[0],[1]]
print(dfs(adj_list))
