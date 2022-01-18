# 연결되지 않은 노드도 존재한다.
# 각 노드에서 다른 노드로 가는 가장 단거리 표를 만든다.  
# (s-> s->A,B) or (s->?->A,B)
import sys
INF = sys.maxsize
import heapq
from collections import defaultdict
def solution(n, s, a, b, fares):
    answer = INF
    # 다익스트라 함수 구현
    d = [[INF] * (n+1) for _ in range(n+1)]

    graph = defaultdict(list)
    for fare in fares:
        graph[fare[0]].append([fare[1], fare[2]])
        graph[fare[1]].append([fare[0], fare[2]])
    
    def dijkstra(start, d):
        q = []
        heapq.heappush(q, [0, start])
        d[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if d[now] < dist: continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < d[i[0]]:
                    d[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    for i in range(1, n+1):
        dijkstra(i, d[i])
        
    for i in range(1, n+1):
        answer = min(answer, d[s][i] + d[i][a] + d[i][b])
    # (s-> s->A,B) or (s->?->A,B)

    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

print(solution(7,3,4,1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))

print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))


















'''

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
'''