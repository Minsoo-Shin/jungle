import sys
INF = sys.maxsize

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

start = 0
end = len(arr) - 1

pair = []
min_val = INF
while start < end:
    total = arr[start] + arr[end]
    # 둘 간의 합을 기존과 비교해 작은걸 채택하고, 두 용액의 산성도도 별도 변수에 저장
    if abs(total) < min_val:
        min_val = abs(total)
        pair = (arr[start], arr[end])

    if total >= 0:
        end -= 1
    else:
        start += 1

print(*pair)
