import sys

n = int(sys.stdin.readline())
ans = [0] * 1000001
ans[0] = 1
ans[1] = 2
div = 15746
for i in range(2, n+1):
    ans[i] = (ans[i-2]%div + ans[i-1]%div)%div

print(ans[n-1]%15746)