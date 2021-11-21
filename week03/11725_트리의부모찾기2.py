import sys
import collections
sys.setrecursionlimit(1000000000)

n = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(n-1):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

parents = [0 for i in range(n+1)] # 인덱스로 접근할 수 있는건 인덱스로 표기
def DFS(graph, node):
    # root들이 연결하고 있는 자식 노드를 확인하고, 저장하고 각각의 자식노드를 또 확인하고 저장하고 재귀..
    for child in graph[node]:
        if parents[child] == 0:
            parents[child] = node
            DFS(graph, child)

DFS(graph, 1)
for i in range(2, n+1):
    print(parents[i])
