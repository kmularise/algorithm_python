def findParent(x):
    if parent[x] == x:
        return x
    #재귀횟수를 줄일 수 있음
    parent[x] = findParent(parent[x])
    return parent[x]

def hasSameParent(x, y):
    x = findParent(x)
    y = findParent(y)
    if x == y:
        return True
    return False

def union(x, y):
    x = findParent(x)
    y = findParent(y)
    if rank[x] > rank[y]:
        parent[y] = x # 트리의 높이는 변화 없음
    elif rank[y] > rank[x]:
         parent[x] = y # 트리의 높이는 변화 없음
    else:
        parent[x] = y #아무거나 상관없음
        rank[x]+=1 #전체 트리 높이 1 증가

V, E = map(int, input().split())
info = []
for i in range(E):
    info.append(list(map(int, input().split())))
#가중치 순서대로 정렬
info.sort(key=lambda x:x[2])
parent = [i for i in range(V)]
rank = [0 for _ in range(V)]
answer = 0
for first, second, cost in info:
	if hasSameParent(first - 1, second -1) == False:
		union(first - 1, second - 1)
		answer += cost
print(answer)