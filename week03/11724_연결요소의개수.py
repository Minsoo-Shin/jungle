import sys
import collections

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

visited = []
def DFS(graph, root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

cnt = 0   
for key in graph.keys():
    a = visited[:] 
    DFS(graph, key)
    if a != visited:
        cnt+=1

print(cnt + n-len(graph))