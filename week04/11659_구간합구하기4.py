import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
d = [0] * (n+1)
# 누적합 구해놓기
for i in range(1, n+1):
    d[i] = nums[i-1] + d[i-1]
# 테스트
for i in range(m):
    s, e = map(int, input().split())
    print(d[e] - d[s-1])
