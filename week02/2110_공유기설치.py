# 이진탐색
# C개의 공유기를 설치하는데 가장 인접한 공유기의 거리를 가장 최대화한다. 
# while 루프의 
n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

result = 0
start = 1
end = arr[-1] - arr[0]
while start <= end:
    mid = (start + end)//2
    current = arr[0]
    count = 1
    for i in range(1,len(arr)):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
