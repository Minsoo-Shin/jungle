import sys
from collections import defaultdict
sys.setrecursionlimit(1000000000)
n = int(sys.stdin.readline().rstrip())
a = list(map(int, list(sys.stdin.readline().strip())))
check = [1]
for i in a:
    check.append(i)

graph = defaultdict(list)

for i in range(n-1):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)


# 실내마다 root를 넣어서 DFS를 넣어주며 경로를 센다. 
cnt = 0
def DFS(start):
    global cnt, visited
    visited[start] = True
    for i in graph[start]:
        if check[i] ==1 and not visited[i]:
            visited[i] = True
            cnt += 1
        elif check[i] ==0 and not visited[i]:
            visited[i] = True
            DFS(i)
    
for i in range(1, n+1):
    visited = [False] * (n + 1)
    if check[i] == 1:
        DFS(i)

print(cnt)