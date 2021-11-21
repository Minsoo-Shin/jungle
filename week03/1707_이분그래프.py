import sys
import collections
sys.setrecursionlimit(1000000000)

# 테스트 케이스의 수를 받아온다. 
n = int(sys.stdin.readline())

# 테스트 케이스대로 실행한다. 
for i in range(n):    
    v, e = map(int, sys.stdin.readline().split()) # V: 노드의 수, E: 간선의 수
    graph = collections.defaultdict(list) # graph 초기화
    for _ in range(e): # 간선의 수만큼 입력값을 받는다. 
        s, e = map(int, sys.stdin.readline().split())
        graph[s].append(e)
        graph[e].append(s)
    print(graph)


def BFS(graph, root):
    visited = [0 for _ in range(n+1)] # 미방문 : 0, 방문&색 : 1, 2
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if visited[node] == 0: # 방문한 적이 없다면 
            visited[node] = 1 # 방문 이력을 남기고 색깔을 기입한다. 
            queue.extend()
            for elem in graph[node]: 
                if visited[node] == visited[elem]:
                    return "NO"



