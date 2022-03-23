'''
1. 아이디어
    - for문을 돌면서
        방문하지 않았고, map에 0이 아닌 곳이라면
            result.append(dfs(i,j))
            vis 
            단지 cnt += 1

2. 시간 복잡도 
    - V : 25 * 25 = 625 E: 4V
    => 5V = 3000

3. 자료 구조
    - graph
    - vis
    - stack

'''
########stack을 이용한 DFS#########
# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(input().split()[0])

# vis = [[False] * n for _ in range(n)]

# def dfs(a, b):
#     stack = [(a,b)]
#     Cnt = 1
#     while stack:
#         x, y = stack.pop()
#         for dx, dy in [[-1,0], [0,1], [1,0] ,[0,-1]]:
#             nx, ny = x + dx, y+dy
#             if nx<0 or ny<0 or nx>=n or ny>=n: continue
#             if vis[nx][ny] == False and graph[nx][ny] != '0':
#                 vis[nx][ny] = True
#                 Cnt += 1
#                 stack.append((nx,ny))
#     return Cnt

# cnt = 0
# result = []
# for i in range(n):
#     for j in range(n):
#         if vis[i][j] == False and graph[i][j] != '0':
#             vis[i][j] = True
#             result.append(dfs(i,j))
#             cnt += 1
# result.sort()
# print(cnt)
# for i in range(cnt):
#     print(result[i])

'''
1. 아이디어
    - for문을 돌면서
        방문이력이 없으면서 and 1인 곳
    - dfs에서 단지 갯수를 result에 넣어라
    - result.sort
    - 단지수, 단지내 집의 수 프린트

2. 시간 복잡도
    - N^2 = 625 

3. 자료구조
    그래프 int[][]
    방문이력 bool[][]
    결과값 int[]

'''
import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]


vis = [[False]*n for _ in range(n)]
result = []
cnt = 0
building = 0

def dfs(x, y):
    global building
    building += 1
    # print(x, y, building)
    for dx, dy in [[-1,0],[0,1],[1,0],[0,-1]]:
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=n or ny<0 or ny>=n: continue
        if vis[nx][ny] == False and map[nx][ny] == 1:
            vis[nx][ny] = True
            dfs(nx, ny)
    

for i in range(n):
    for j in range(n):
        if vis[i][j] == False and map[i][j] == 1:
            vis[i][j] = True
            building = 0
            # print(i,j,'시작')
            dfs(i,j)
            result.append(building)
            cnt += 1

result.sort()
print(cnt)
for i in range(len(result)):
    print(result[i])
