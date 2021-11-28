import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    unit_ea = int(input())
    units = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1
    for unit in units:
        for val in range(unit, target + 1):
            dp[val] += dp[val-unit] 

    print(dp[target])
    