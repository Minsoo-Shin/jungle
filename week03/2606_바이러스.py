import sys
import collections 
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = collections.defaultdict(list)
for _ in range(m):
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
            stack.extend(list(set(graph[node])-set(visited)))

DFS(graph, 1)
print(len(visited)-1)