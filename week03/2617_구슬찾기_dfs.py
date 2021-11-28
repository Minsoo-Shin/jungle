import sys

n, m = map(int, sys.stdin.readline().split())
graph_b = [[]*(n+1) for _ in range(n+1)]
graph_s = [[]*(n+1) for _ in range(n+1)]
mid = n//2

for i in range(m):
    b, s = map(int, sys.stdin.readline().split())
    graph_b[s].append(b)
    graph_s[b].append(s)
 

def DFS(start, graph):
    visited = [False] * (n+1)
    stack = [start]
    visited[start] = True
    cnt = 0
    while stack:
        num = stack.pop()
        for i in graph[num]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                cnt += 1
                if cnt > mid:
                    return 1
    return 0

ans = 0
for i in range(1, n+1):
    ans += DFS(i, graph_s)
    ans += DFS(i, graph_b)
print(ans)
