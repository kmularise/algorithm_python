import heapq
def dijkstra(start):
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        distance, current = heapq.heappop(heap)
        for next, weight in graph[current]:
            if distance + weight < dist[next]:
                dist[next] = distance + weight
                heapq.heappush(heap, (dist[next], next))

V, E = map(int, input().split())
start = int(input())
INF = 10 ** 9
dist = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
dijkstra(start)
for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])