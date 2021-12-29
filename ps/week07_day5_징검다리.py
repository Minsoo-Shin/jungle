# 라우터 갯수를 기준으로 
# left/right/mid : 최소 거리 값
# mid를 최댓값으로 계속 갱신

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks = [0] + rocks + [distance]
    left, right = 1, distance
    while left <= right:
        mid = (left + right)//2
        cur = rocks[0]  #초기값
        cnt = 1
        for i in range(1, len(rocks)):
            if rocks[i] - cur >= mid:
                cur = rocks[i]
                cnt += 1
        if cnt >= len(rocks) - n:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
            
    return answer

# print(solution(25, [2,14,11,21,17], 2))
print(solution(25, [2,14,11,21,17], 0))