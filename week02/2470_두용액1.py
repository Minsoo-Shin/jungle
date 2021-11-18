# 메모리 초과
n = int(input())

arr = list(map(int, input().split()))
arr.sort()
n = len(arr)
start = max([arr[0] + arr[1], arr[-2] + arr[-1]])

end = 0
result = {}
while start >= end:
    mid = (start + end)//2
    for i in range(n):
        for j in range(n-1, i, -1):
            abs_value = abs(arr[i] + arr[j])
            if abs_value <= mid:
                start = mid - 1
                result[abs_value] = [arr[i], arr[j]]
            else:
                end = mid + 1 

print(*result[min(result)])