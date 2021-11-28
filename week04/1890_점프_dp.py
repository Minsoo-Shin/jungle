# DP를 이용한 방법
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
M = [list(map(int, input().split())) for _ in range(n)]
D = [[0] * n for _ in range(n)]


for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if 0 <= i <= n-1 and 0 <= j <= n-1:
            if j + M[i][j] < n:
                D[i][j] += D[i][j + M[i][j]]
            if i + M[i][j] < n:
                D[i][j] += D[i + M[i][j]][j]
        D[n-1][n-1] = 1
print(D[0][0])