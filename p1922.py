def findParent(x):
    if parent[x] == x:
        return x
    parent[x] = findParent(parent[x])
    return parent[x]

def union(x, y):
    x = findParent(x)
    y = findParent(y)
    if x == y:
        return -1
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[y] > rank[x]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x]+=1
    return 0

V = int(input())
E = int(input())
edgeData = []
for i in range(E):
    edgeData.append(list(map(int, input().split())))

edgeData.sort(key = lambda x:x[2])
parent = [i for i in range(V + 1)]
rank = [0 for i in range(V + 1)]
cost = 0
for vertex1, vertex2, weight in edgeData:
    if union(vertex1, vertex2) == 0:
        cost += weight
print(cost)
