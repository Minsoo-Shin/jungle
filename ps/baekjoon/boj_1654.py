# n : 가진 전선
# m : 필요한 갯수의 전선
# length : 각각 랜선의 길이 리스트
#

n, m = map(int, input().split())
length = [int(input()) for _ in range(n)]
length.sort()
# 필요한 갯수의 크기를 기준으로
# 최대 랜선의 길이를 구하는 프로그램

# 잘라서 나눈 길이
left = 1
right = sum(length)
ans = 0
while left <= right:
    mid = (left + right)//2
    l = 0
    for len in length:
        l += (len // mid) # 고정된 크기로 잘랐을때의 갯수
        if l >= m:
            break
    if l >= m:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(ans)
