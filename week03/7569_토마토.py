import sys
from collections import deque
INF = int(1e9)
m, n, h = map(int, sys.stdin.readline().split())

arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
ripe = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                ripe.append((i, j, k))

visited = [[[False] * n for _ in range(n)] for _ in range(h)]
day = 0
q = deque()
q.append(ripe)

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while q:
    z, x, y = q.popleft()
    visited[z][x][y] = True
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<= nx <= n-1 and 0<= ny <= m-1 and 0<= nz <= h-1:
            if not visited[nz][nx][ny]  and arr[nz][nx][ny] != 1 and arr[nz][nx][ny] != -1:
                visited[nz][nx][ny] = True
                arr[nz][nx][ny] = 1
                q.append((nz, nx, ny))

