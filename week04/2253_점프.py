'''
1. 돌 번호가 증가하는 순서대로 점프가능
2. 첫 점프는 1, 그 뒤로 x-1, x, x+1칸 만큼 점프 가능 (단, 점프는 한 칸 이상)
3. 몇개의 돌 위에는 올라갈 수 없다. 
'''
import sys
N, M = map(int, sys.stdin.readline().split())
dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)] 
dp[1][0] = 0

stone_set = set()
for _ in range(M):
    stone_set.add(int(sys.stdin.readline()))
for i in range(2, N + 1):
    if i in stone_set:
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
        print(dp[i - j][j - 1])
        print(dp[i - j][j])
        print(dp[i - j][j + 1])
if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))