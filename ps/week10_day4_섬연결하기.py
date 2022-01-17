# 다리를 건설하는 비용 costs, 최소비용으로 통행하도록
# 섬은 100이하
# [0, 1, 1] 0~1 1 비용이 든다. 
# 모든 섬의 다리 건설 비용이 주어지지 않는다. 이는 건설이 불가
# 연결할 수 없는 섬은 없다. 

# union find 문제
# 어느 위치에서 가장 작은 위치를 선택한다. 
import sys
INF = sys.maxsize
from collections import defaultdict

def solution(n, costs):
    graph = defaultdict(list)
    for cost in costs:
        graph[cost[0]].append([cost[1], cost[2]])
        graph[cost[1]].append([cost[0], cost[2]])
    print(graph)
    min_value = INF    

    def dfs(start):
        total_cost = 0
        visited = [False]*n
        while start: 
            s = start.pop()
            visited[s] = True
            min_list = []
            for val in graph[s]:
                next, cost = val[0], val[1]
                if not min_list: min_list.append([next, cost])
                elif min_list[0][1] > cost:
                    min_list.pop()
                    min_list.append([next, cost])
                else: continue
            next, cost = min_list.pop()
            if visited[next] == False:
                visited[next] = True
                total_cost += cost
                start.append(next)
        if all(visited):
            return total_cost
        else:
            return 100

    for i in range(n):
        min_value = min(min_value, dfs([i]))
    return min_value

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

        



        

