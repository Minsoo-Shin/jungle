import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)
q = deque()
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:
        q.appendleft(i) #inDegree 진입 차수가 0인 노드를 고른다. 

while q:
    node = q.popleft()
    print(node, end=" ")
    for d in graph[node]:
        inDegree[d] -= 1 #
        if inDegree[d] == 0:
            q.append(d)
