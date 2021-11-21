import sys
import collections

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (n+1)
def DFS(graph, root):
    stack = [root]
    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = True
            stack += graph[node]

cnt = 0   
for key in graph.keys():
    if visited[key] == 0:
        cnt+=1
        DFS(graph, key)

print(cnt + n-len(graph))