# N개의 회의를 배정하는데 배정할 수 있는 최대 회의 개수
# 예외) 회의 시작시간과 끝나는 시간 같을 수도
# N: 회의의 수
# 회의의 정보 (시작 종료 시간)

import sys
input = sys.stdin.readline

n = int(input())
time = []
# [ [1,4] ,[3,5], [0,6], [5,7] ....]
for i in range(n):
    time.append(list(map(int, input().split())))

time.sort(key = lambda x: (x[1], x[0]))

time_table = [time[0]]
cnt = 1
for i in range(1, n):
    if time[i][0] >= time_table[-1][1]:
        time_table.append(time[i])
        cnt += 1

ans = cnt
print(ans)