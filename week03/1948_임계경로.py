import sys
import heapq 
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
graph_back = [[] for _ in range(n+1)]
for i in range(m):
    s, e, cos = map(int, input().split())
    graph[s].append((e, cos))
    graph_back[e].append((s, cos))
s, e = map(int, input().split())
time = [0] * (n+1)

def dijkstar(start):
    q = []
    heapq.heappush(q, (0, start))    
    # start가 주어지면 그 노드의 거리를 초기화해준다. 
    time[start] = 0
    while q:
        # 시작 노드 정보를 변수에 대입
        neg_cost, city = heapq.heappop(q)
        # 초기화된 정보나 기존 정보가 더 크다고 하면 넘어간다. 
        if time[city] > -neg_cost: continue
        # 인접해있는 모든 노드를 탐색해서 제일 코스트가 큰 쪽으로 간다. 
        for next in graph[city]:
            # 다음 시티와 비용을 저장한다. 
            next_city, next_cost= next[0], next[1]
            # 이전 도시까지 걸린 비용 + 다음 도시 기존 비용
            more_time = time[city] + next_cost
            # 한번에 다음 도시로 가는 비용과 비교해서 거쳐서 오는게 더 많이 걸리면 갱신
            if time[next_city] < more_time:
                time[next_city] = more_time
                # 다음 도시 가는 곳은 힙으로 다시 저장
                heapq.heappush(q, (-more_time, next_city))
    return time[e]
print(dijkstar(s))

# 그래프_back의 시작점과 인접한 도시. 각각의 끝점까지의 시간은 구해져있고, time.
# time(끝점) - time(인접) = graph상 거리가 같은지 계속 확인한다. 이는 가장 오래 걸린 시간으로 갱신해놨으므로 이것과 맞는 길인지 탐색

q = deque()
q.append(e)
ans = 0
while q:
    visited = [False] * (n+1)
    node = q.popleft()
    visited[node] = True
    for bef, cost in graph_back[node]:
        if not visited[bef]:
            if time[node] - time[bef] == cost:
                ans += 1
                q.appendleft(bef)
            
print(ans)