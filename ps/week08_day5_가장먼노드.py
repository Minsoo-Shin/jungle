import heapq
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for e in edge:
        graph[e[0]].append((e[1], 1))
        graph[e[1]].append((e[0], 1))

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

    dijkstra(1)

    answer = 0
    max_value = 0
    for i in range(len(distance)):
        if distance[i] == INF: continue
        if distance[i] > max_value:
            max_value = distance[i]
            answer = 1
        elif distance[i] == max_value:
            answer += 1
            
    return answer
    

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))