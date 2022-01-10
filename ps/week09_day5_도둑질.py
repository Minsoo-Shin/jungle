# 내 풀이 실패
def solution(money):
    n = len(money)
    d = [0] * n

    if n % 2 == 0:
        d[0], d[1] = money[0], money[1]
        for i in range(2, n):
            d[i] = max(d[i-1], d[i-2]+ money[i])
    else:
        d[0], d[1] = money[0], max(money[0], money[1])
        for i in range(2, n-1):
            d[i] = max(d[i-1], d[i-2]+ money[i])
        d[n-1] = max(d[n-2], d[n-3] + money[n-1] - d[0])
                
    return d[n-1]
print(solution(  [1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000]))

#반례) print(solution([10, 2, 2, 100, 2]))


def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money)-1): # 첫 집을 무조건 터는 경우
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)): # 마지막 집을 무조건 터는 경우
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    return max(max(dp1), max(dp2)) # 두 경우 중 최대

print(solution( [1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]))
print(solution( [1000, 1, 0, 1, 2, 1000, 0]))