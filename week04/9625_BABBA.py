k = int(input())
d = [[0,0]] * 46
d[0] = [1,0]

for i in range(1, k+1):
    a, b = d[i-1]
    d[i] = [b, a+b]

print(*d[k])
