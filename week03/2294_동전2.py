import sys
input = sys.stdin.readline
INF = sys.maxsize
n, k = map(int, input().split())
a = [int(input().rstrip()) for _ in range(n)]
a.sort()
print(a)
min_cnt = INF
ispossible = False

for i in range(1, n+1):
    coin = 0
    num = k
    for j in range(i-1, -1, -1):
        coin += num // a[j]
        num = num % a[j]
        if num == 0:
            ispossible = True
            min_cnt = min(min_cnt, coin)
            break

if ispossible == True:
    print(min_cnt)
else:
    print(-1)

'''
앞에서 부터 분할해서 생각해보자
3 15
[1, 5, 12]

- 1만 있는 경우
15 // 1 = 15개 
min_cnt = 갱신

- 1, 5만 있는 경우
15 // 5 = 3개
min_cnt = 갱신

- 1, 5, 12 만 있는 경우
15 // 12 = 1개
15 % 12 // 5 = 0개
15 % 12 % 5 // 1 = 3개 

불가능한 경우에는 -1을 출력한다. 
예제)
2 7
[2, 3]

반례) 
3 12
[10,4,2]
정답 2
'''
