n, m = map(int, input().split())
d = [[] for _ in range(n+1)]
d[0] = [1]
d[1] = [1,1]
# 점화식
for i in range(2,n+1):
    for j in range(1, len(d[i-1])):
        d[i].append(d[i-1][j-1] + d[i-1][j])
    d[i] = [1] + d[i] + [1]

print(d[n-1][m-1])