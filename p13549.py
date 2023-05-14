import heapq
from collections import defaultdict
def dijkstra(start):
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        distance, node = heapq.heappop(heap)
        if node == K:
            break
        if 0 <= node * 2 and node * 2 <= 100000 and distance < dist[node * 2]:
            dist[node * 2] = distance
            heapq.heappush(heap, (distance, node * 2))
        if 0 <= node + 1 and node + 1 <= 100000 and distance + 1 < dist[node + 1]:
            dist[node + 1] = distance + 1
            heapq.heappush(heap, (distance + 1, node + 1))        
        if 0 <= node - 1 and node - 1 <= 100000 and distance + 1 < dist[node - 1]:
            dist[node - 1] = distance + 1
            heapq.heappush(heap, (distance + 1, node - 1))
    

N, K = map(int, input().split())
INF = 10 ** 9
dist = [INF] * 1000001
dijkstra(N)
print(dist[K])
