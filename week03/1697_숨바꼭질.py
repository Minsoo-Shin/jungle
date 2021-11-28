import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
def sol(method, x):
    if method == '-1':
        result = x - 1
    elif  method == '+1':
        result = x + 1
    else:
        result = x * 2
    return result

def bfs(n, k):
    q = deque([n])
    visited = [0] * 200001
    visited[n] = 0
    while q:
        node = q.popleft()
        for i in ['-1', '+1', '*2']:
            res = sol(i, node)
            if res >= 2 * k or res < 0: continue
            if visited[res] == 0:
                visited[res] = visited[node] + 1
                q.append(res)
            if res == k:
                return visited[k]
    return visited[k]

if n >= k:
    ans = n-k
else:
    ans = bfs(n,k)

print(ans)

'''
반례)
2 0
k가 0일 경우 문제가 되는 경우

반례)
1 1

'''