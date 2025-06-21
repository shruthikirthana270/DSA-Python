def dfs(i,j,grid,visited,n,m):
    visited[i][j]=1
    for row,col in [[-1,0],[1,0],[0,-1],[0,1]]:
        delRow=i+row
        delCol=j+col
        if(delRow>=0 and delRow<n and
        delCol>=0 and delCol<m and
        grid[delRow][delCol]=="1" and visited[delRow][delCol]==0):
            dfs(delRow,delCol,grid,visited,n,m)
def numIslands(grid):
    n=len(grid)
    m=len(grid[0])
    visited=[]
    for i in range(n):
        temp=[0]*m
        visited.append(temp)
    c=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="1" and visited[i][j]==0:
                dfs(i,j,grid,visited,n,m)
                c+=1
    return c
n,m=map(int,input().split())
grid=[]
for i in range(n):
    row=input().strip().split()
    grid.append(row)
print(numIslands(grid))
