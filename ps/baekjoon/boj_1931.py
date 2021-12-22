# 회의실 배정

# 회의시간 시작시간 끝나는 시간이 주어지고, 
# 스케쥴 상 가장 많이 들어갈 수 있는 회의의 수

# 코드 설명
# 끝나는 시간을 기준으로 오름차순 정렬을 하고,
# 순차적으로 확인하면서 안겹치는 회의가 나타났을 때, cnt += 1

import sys
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))
ans = 1
last_time = [meetings[0]]

# sortedx by finishing time
for i in range(1, len(meetings)):
    # compare previous meeting finishing time with current meeting starting time
    if meetings[i][0] >= last_time[-1][1]:
        ans += 1
        last_time.append(meetings[i])
print(ans)


        
    