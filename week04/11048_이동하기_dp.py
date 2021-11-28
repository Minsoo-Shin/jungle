import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
dp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for j in range(m):
    for i in range(n):
        if i == 0 and j != 0:
            dp[i][j] += dp[i][j-1]
            
        elif i != 0 and j == 0:
            dp[i][j] += dp[i-1][j]
        
        elif 0 < j < m and 0 < i < n:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])

print(dp[n-1][m-1])