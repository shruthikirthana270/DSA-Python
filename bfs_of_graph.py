#bfs traversal of a graph
def bfs(adj):
    v=len(adj)
    visited=[0]*v
    startnode=0
    ans=[]
    q=[]
    if(visited[startnode]==0):
        visited[startnode]=1
        q=[startnode]
        while(q):
            node=q.pop(0)
            ans.append(node)
            for i in adj[node]:
                if(visited[i]==0):
                    visited[i]=1
                    q.append(i)
        return ans
adj = [[1, 4],[0, 2, 3, 4],[1, 3],[1, 2, 4],[0, 1, 3]]
print(bfs(adj))
    
    
