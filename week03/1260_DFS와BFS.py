import sys
import collections

n, m, v = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)

for _ in range(m):
    s,e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)
    graph[s].sort(key= lambda x: -x)
    graph[e].sort(key= lambda x: -x)

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited

def BFS(graph, root):
    visited = []
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
print(*DFS(graph, v))

for key in graph.keys():
    graph[key].sort(key= lambda x: x)
    graph[key].sort(key= lambda x: x)
print(*BFS(graph, v))

