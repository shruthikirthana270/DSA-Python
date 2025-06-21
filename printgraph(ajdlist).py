"""def printgraph(v,edges):
    adjList=[]
    for i in range(v):
        adjList.append([])
        for n,m in edges:
            adjList[n].append(m)
            adjList[m].append[n]
        for lst in adjList:
            lst.sort()
        return adjList
===============================================================



def printgraph(v, edges):
    adjList = []
    for i in range(v):
        adjList.append([])

    for n, m in edges:
        adjList[n].append(m)
        adjList[m].append(n)

    for lst in adjList:
        lst.sort()

    return adjList

# Input
v = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
adj = printgraph(v, edges)
for i in range(v):
    print(f"{i}: {adj[i]}")
    ==================================="""
def printgraph(v, edges):
    adjList = []
    for i in range(v):
        adjList.append([])

    for n, m in edges:
        adjList[n].append(m)
        adjList[m].append(n)

    for lst in adjList:
        lst.sort()

    return adjList

# Input
v = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
print(printgraph(v, edges))














    
