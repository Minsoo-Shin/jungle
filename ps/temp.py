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
        #반례 : [5,3,1,4,10] dp[n-3]이 money[n-3]을 픽할수도 있고 안할수도 있어서 경우가 나뉘어짐
        for i in range(2, n-1):
            d[i] = max(d[i-1], d[i-2]+ money[i])
        d[n-1] = max(d[n-2], d[n-3] + money[n-1] - d[0])
                
    return d[n-1]

print(solution([5,3,1,4,10]))