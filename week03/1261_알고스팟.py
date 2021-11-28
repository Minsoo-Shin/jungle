import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
miro = [list(map(int, list(input().rstrip()))) for _ in range(m)]
cost = [[0] * (n) for _ in range(m)]

def bfs(x, y):
    q = []
    heapq.heappush(q, (1, x, y))
    cost[x][y] = 1
    while q:
        cos, x, y = heapq.heappop(q)
        for dx, dy in ((-1,0), (0,1), (1,0), (0,-1)):
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
            if cost[nx][ny] == 0:
                if  miro[nx][ny] == 0:
                    cost[nx][ny] = cos
                elif miro[nx][ny] != 0:
                    cost[nx][ny] = cos + 1
                heapq.heappush(q, (cost[nx][ny], nx, ny))
    
bfs(0,0)
print(cost[m-1][n-1]-1)

