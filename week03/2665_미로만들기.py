import sys
import heapq
INF = int(1e9)

n = int(sys.stdin.readline().strip())

miro = [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(n)]
t_cost = [[INF] * (n) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dijkstra(r, c):
    q = []
    heapq.heappush(q, (0, r, c))
    t_cost[r][c] = 0
    while q:
        cost, row, col = heapq.heappop(q)
        visited[row][col] = True

        if t_cost[row][col] < cost:
            continue

        if row == n-1 and col == n-1:
            return t_cost[n-1][n-1]

        for dx, dy in ((-1,0), (0,1), (1,0), (0, -1)):
            nx = row + dx
            ny = col + dy
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if miro[nx][ny] != 0: #nx와 ny가 방문한 적이 없으며, miro상에서도 흰방일 경우, cost는 1만 더한다. 
                    tmp = cost 
                    if tmp < t_cost[nx][ny]:
                        t_cost[nx][ny] = tmp
                        heapq.heappush(q, (tmp, nx, ny))

                elif miro[nx][ny] == 0:  #nx와 ny가 방문한 적이 없으며, miro상에서도 검은 방일 경우, cost는 2를 더한다. (핸디캡) 
                    tmp = cost + 1
                    if tmp < t_cost[nx][ny]:
                        t_cost[nx][ny] = tmp
                        heapq.heappush(q, (tmp, nx, ny))

print(dijkstra(0,0))
