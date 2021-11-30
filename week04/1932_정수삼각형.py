import sys
input = sys.stdin.readline

n = int(input())
a = [[]] * n # [[], [], [], [].....]
d = [[]] * n

for i in range(n):
    d[i] = [0] * (i+1)

for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1):
        if j == 0:
            d[i][j] = d[i-1][0] + a[i][0]
        elif j == i:
            d[i][j] = d[i-1][i-1] + a[i][i]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + a[i][j]

print(max(d[n-1]))

# 맨 왼쪽, 오른쪽 외엔 대각선 왼쪽위, 오른쪽위가 다 있다. 
# d[i][j] = max(d[i-1][j], d[i-1][j+1])

# 맨 왼쪽은 d[i][0] = d[i-1][0] + a[i][0], d[i][-1] 