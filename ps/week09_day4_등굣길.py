
from collections import deque

def solution(m, n, puddles):
    answer = 0
    que = deque([[0,0]])
    xbox = [[True]*m for _ in range(n)]
    for a, b in puddles:
        xbox[b-1][a-1] = False
    while que:
        x, y = que.popleft()
        for dx, dy in [[1,0], [0,1]]:
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<m  and xbox[nx][ny] != False:
                if nx == n-1 and ny == m-1:
                    answer += 1
                    continue
                que.append([nx, ny])    
    return answer % 1000000007

print(solution(4,3, [[2,2]]))


# def solution(m, n, puddles):
#     dp = [[0]*m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if i == 0 and j == 0:
#                 dp[i][j] = 1
#             elif i == 0:
#                 dp[i][j] = 1
#             elif j == 0:
#                 dp[i][j] = 1

#     xbox = [[True]*m for _ in range(n)]
#     for x, y in puddles:
#         xbox[x-1][y-1] = False

#     for i in range(1, n):
#         for j in range(1, m):
#             # [i, j] 가 웅덩이가 있으면 continue
#             if xbox[i][j] == False: continue
#             # 왼쪽만 웅덩이가 있으면 
#             elif xbox[i-1][j] == True and xbox[i][j-1] == False:
#                 dp[i][j] = dp[i-1][j]
#             # 위쪽만 웅덩이가 있으면
#             elif xbox[i-1][j] == False and xbox[i][j-1] == True:
#                 dp[i][j] = dp[i][j-1]
#             # 둘 다 웅덩이가 없으면 
#             elif xbox[i-1][j] == True and xbox[i][j-1] == True:
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#             # 둘 다 웅덩이가 있으면 
#             else:
#                 dp[i][j] = 0
#     return dp[n-1][m-1] 
                
# print(solution(4,3, [[2,2]]))

# def solution(m, n, puddles):
#     dp = [[0]*m for _ in range(n)]
#     xbox = [[True]*m for _ in range(n)]
#     for x, y in puddles:
#         xbox[x-1][y-1] = False
#     # 가장자리에 있는 경우

#     for x in range(n):
#         for y in range(m):
#             if x==0 and y==0:
#                 dp[x][y] = 1
#             if xbox[x][y] == False: continue
#             else:
#                 if x==0 and 0<y<m:
#                     dp[x][y] = dp[x][y-1]
#                 elif 0<x<n and y==0:
#                     dp[x][y] = dp[x-1][y]
#                 elif 0<x<n and 0<y<m:
#                     dp[x][y] = dp[x-1][y] + dp[x][y-1]
    
#     return dp[n-1][m-1] % 1000000007

# print(solution(4,3, [[2,2]]))


def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    xbox = [[True]*(m+1) for _ in range(n+1)]
    for x, y in puddles:
        xbox[y][x] = False

    for x in range(1, n+1):
        for y in range(1, m+1):
            if x==1 and y==1:
                dp[x][y] = 1
                continue
            if xbox[x][y] == False:
                dp[x][y] = 0
            else:
                dp[x][y] = (dp[x-1][y] + dp[x][y-1])% 1000000007
    
    return dp[n][m]


def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]

    for x in range(1, n+1):
        for y in range(1, m+1):
            if x==1 and y==1:
                dp[x][y] = 1
                continue
            if [x,y] in puddles:
                dp[x][y] = 0
            else:
                dp[x][y] = (dp[x-1][y] + dp[x][y-1])% 1000000007

    return dp[n][m]

print(solution(4,3, [[2,2]]))