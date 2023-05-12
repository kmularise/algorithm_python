import heapq
import sys
input =sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 첫번째 요소를 우선순위로 정렬해서 넣는다.
    dis[start] = 0
    while q:
        distance, node = heapq.heappop(q)# 거리를 뽑아냄
        if dis[node] < distance: #크기 비교
            continue
        for v, w in graph[node]:
            cost = distance + w
            if cost < dis[v]: #기존의 거리보다 작아야 넣는 의미가 있다.
                dis[v] = cost
                heapq.heappush(q, (cost, v))


V, E = map(int, input().split())
start = int(input())
INF = 10 ** 9
dis = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
dijkstra(start)
for i in range(1, V + 1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])