'''
아이디어: 이중 for문을 돌면서 bfs순회를 한다. cnt += 1, return으로 넓이
    이미 방문했거나 그림 1인 지점만 돌면서 체크

시간 복잡도: vertex 500 * 500, edge = 4 v
            => 5v = 250000 * 5 = 125만

자료구조: 
    1. map
    2. visit
    3. queue
'''


import sys
from collections import deque
imput = sys.stdin.readline

n, m = map(int, input().split())
map = [ list(map(int, input().split())) for _ in range(n) ]
vis = [ [False] * m for _ in range(n) ]

def bfs(a, b):
    q = deque([[a,b]])
    s = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [ [-1,0],[0,1],[1,0],[0,-1] ]:
            nx, ny = x + dx, y + dy
            print(nx, ny)
            if nx <0 or ny <0 or nx >=n or ny >= m: continue
            if vis[nx][ny] == False and map[nx][ny] == 1:
                vis[nx][ny] = True
                q.append([nx,ny])
                s += 1
    return s


cnt = 0
maxv = 0
for i in range(n):
    for j in range(m):
        if vis[i][j] == False and map[i][j] == 1:
            vis[i][j] = True
            cnt += 1
            maxv = max(maxv, bfs(i,j))

print(cnt)
print(maxv)

