#이진탐색
n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
print(n, c)
print(arr)

pl = 0
pr = max(arr) - 1

while c > 0:
    pc = (pl + pr)//2
     