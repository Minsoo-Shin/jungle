# 회의실 배정

# 회의시간 시작시간 끝나는 시간이 주어지고, 
# 스케쥴 상 가장 많이 들어갈 수 있는 회의의 수

# 코드 설명
# 끝나는 시간을 기준으로 오름차순 정렬을 하고,
# 순차적으로 확인하면서 안겹치는 회의가 나타났을 때, cnt += 1

# import sys
# input = sys.stdin.readline

# n = int(input())
# meetings = [list(map(int, input().split())) for _ in range(n)]
# meetings.sort(key=lambda x: (x[1], x[0]))
# ans = 1
# last_time = [meetings[0]]

# # sortedx by finishing time
# for i in range(1, len(meetings)):
#     # compare previous meeting finishing time with current meeting starting time
#     if meetings[i][0] >= last_time[-1][1]:
#         ans += 1
#         last_time.append(meetings[i])
# print(ans)


# 끝지점으로 정렬하게 하고, 최대한 많이 참여해야함
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
# [s, e] 두 번째 기준으로 하면 문제 없을거 같다. 
# 첫번째 기준에 대한 정렬 기준이 없다면? 
    # [10, 10], [5, 10]와 같이 주어질 때, 하나로 계산되지만, 
    # 첫 번째 기준을 오름차순으로 줬다면? [5, 10], [10,10]으로 두개로 계산됨
    # 첫 번째 기준은 반드시 필요하다. 
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
arr.sort(key = lambda x: (x[1], x[0]))
# 돌면서 다음회의 시작시간이 현재의 회의 마지막시간보다 낮다면
last = 0
for start, end in arr:
    if last > start: continue
    last = end
    ans += 1

print(ans)


























    