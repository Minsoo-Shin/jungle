import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x, y, w = q.popleft()
        for dx, dy in ((-1,0), (0,1), (1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if a[nx][ny] == 'D':
                if w: continue
                return dist[x][y] # 당연히 D에는 dist 기록이 없기 떄문에 x, y의 값으로 출력
            if dist[nx][ny] or a[nx][ny] == 'X': continue #방문기록이 있거나 x라면 진행x
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny,w))
    return "KAKTUS"

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
q = deque()
dist = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            x, y = i, j
            dist[i][j] = 1 # 마지막 한 칸을 안간 채로 print하기 때문에
        elif a[i][j] == '*':
            q.append((i, j, 1))
            dist[i][j] = 1
q.append((x, y, 0))

print(bfs())