def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x == y:
        return
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[y] < rank[x]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1

import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    for j in range(1, N + 1):
        if line[j - 1] == 1:
            union(i, j)
plan = list(map(int, input().split()))

prev = plan[0]
answer = "YES"
for ele in plan:
    if find_parent(prev) != find_parent(ele):
        answer = "NO"
    prev = ele
print(answer)
