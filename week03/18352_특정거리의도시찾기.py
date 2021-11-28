import sys
import heapq
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(x)

ans = []
for i in range(n+1):
    if distance[i] == k:
        print(i)
        ans.append(i)
    
if len(ans) == 0:
    print(-1)

    