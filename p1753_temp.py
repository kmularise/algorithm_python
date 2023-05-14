import sys
import heapq
sys.setrecursionlimit = 10 ** 6

def dijkstara(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        distance, node = heapq.heappop(q)
        # if dis[node] < distance:
        #     continue
        for v, w in graph[node]:
            next_distance = distance + w
            if next_distance < dis[v]:
                dis[v] = next_distance
                heapq.heappush(q, (next_distance, v))


V, E = map(int, input().split())
start = int(input())
INF = 10 ** 9
dis = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]
for i in range (E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
dijkstara(start)
for i in range(1, V + 1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])