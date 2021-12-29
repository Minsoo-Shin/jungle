# 이분탐색
# mid : 자르는 높이
# 나무가 자르는 높이가 큰 경우에만 그 길이를 더하고 변수에 더한다. 
# if  >= mid
#    left = mid + 1
# else : right = mid - 1


n, m = map(int, input().split())
tree = list(map(int, input().split()))
ans = 0

start = 0
end = max(tree)
while start <= end:
    mid = (start + end)//2
    cut = 0 
    for tr in tree:
        if tr > mid: 
            cut += tr - mid
    # 경계값 조정
    if cut >= m: 
        ans = max(ans, mid)
        start = mid + 1
    else: end = mid - 1

print(ans)