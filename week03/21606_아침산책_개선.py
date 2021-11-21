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

def permutation(n: int, c: int) -> int:
    if c == 0:
        return 1
    return n * permutation(n-1,c-1)

def DFS_find_outin(start: int, CheckPoint: int) -> int: #실외 기준으로 탐색
    global visited
    cnt=0
    if CheckPoint == 0: # 야외와 연결된 모든 실내
        visited[start] = True
        for i in graph[start]:
            if not visited[i]:
                if check[i] == 1:
                    #visited[i] = True
                    cnt += 1
                elif check[i] == 0:
                    #visited[i] = True
                    cnt += DFS_find_outin(i, 0)
        return cnt 
    else: # CheckPoint == 1 일때, 실내 - 실내 
        for i in graph[start]:
                if check[i] == 1:
                    cnt += 1
        return cnt

visited = [False] * (n+1)
ans = 0
for i in range(1, n+1):
    if check[i] == 0 and not visited[i]: #실외인 것만 실행
        tmp = permutation(DFS_find_outin(i, 0),2)
        ans += tmp
for i in range(1, n+1):
    if check[i] == 1:
        tmp = DFS_find_outin(i, 1)
        ans += tmp
print(ans)