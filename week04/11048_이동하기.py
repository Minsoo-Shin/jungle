# 90%대에서 틀렸습니다. 예외 케이스 존재

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
d = [[0]*m for i in range(n)]
q = deque()
q.append((a[0][0], 0, 0))
d[0][0] = a[0][0]
while q:
    candy, r, c = q.popleft()
    for dr, dc in ((1,0),(0,1),(1,1)):
        nr = r + dr
        nc = c + dc
        if nr < 0 or nc < 0 or nr >= n or nc >= m: continue
        if d[r][c] + a[nr][nc] > d[nr][nc]:
            d[nr][nc] = d[r][c] + a[nr][nc]
            q.append((d[nr][nc], nr, nc))

print(d[n-1][m-1])
