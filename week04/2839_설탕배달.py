n = int(input()) #18,   3kg, 5kg

array = [3, 5]
d = [5001] * (n+1)
d[0] = 0

for i in array:
    for j in range(i, n+1):
        d[j] = min(d[j], d[j-i] + 1)

if d[n] == 5001:
    print(-1)
else:
    print(d[n])