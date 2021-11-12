n, M = map(int, input().split()) #n(int형) : 나무 갯수, M(int형) : 가져가야할 나무 길이
arr = list(map(int, input().split()))
pl = 0
pr = max(arr)
result = []
while True:
    ssum = 0
    pc = (pl + pr)//2
    for i in range(n):
        differ = arr[i] - pc
        if differ > 0:
            ssum += differ
    if ssum >= M:
        result.append(pc)
        pl = pc + 1
        
    else:
        pr = pc - 1
    if pl > pr:
        break


print(max(result))