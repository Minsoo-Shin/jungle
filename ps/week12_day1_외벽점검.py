# [1.5.6.10] 
#     0  1  2  3
#  0 [0, 4, 5, 4] min 4
#  1 [4, 0, 1, 5] min 1
#  2 [5, 1, 0, 4] min 1
#  3 [4, 5, 4, 0] min 4

# 제일 멀리 갈 수 있는 사람이 많은 지점을 거치게 해야한다. 
    # 거칠 수 있는 지점의 수가 같다면, 

# 인부의 수를 고정해서 완전탐색을 하면서 인부의 수를 낮춰간다. 
# 인부의 수가 1일 경우, 모든 시작 위치에서 갈 수 있는지를 확인한다. 
    # 해당 위치 기준으로 최소 거리를 확인하면 된다. 
# 인부의 수가 2일 경우, 

# def rm_weak(remainder)
    # return remainder 
# 
# 가장 많이 돌 수 있는 인부가 최대한 많이 제거해야한다.
# for 인부
#   def rm_weak으로 나온 결과 리스트의 수가 
#   1차 리스트가 없다면 return cnt
#   2차 적은 수는 모두 stack에 저장하고 다시 돌린다.
#  한번 다 돌리고 나면 인부의 cnt를 += 1
# 
# from collections import defaultdict
# from dis import dis

# def solution(n, weak, dist):
#     answer = 0
#     dist.sort(reverse = True)
#     # 한 인부로 최대로 점검하여 점검 못한 리스트 줄이기
#     def rm_weak(d, remainder):
#         result = defaultdict(list) # {'1' : [rem1, rem2], '2' : ...}
#         # 갈 수 있는 거리 d와 출발점이 주어지면 지워야할 범위를 구할 수 있다. 
#         for start in remainder:
#             include = []
#             dist_from_start = [0] * len(remainder)
#             for i in range(len(remainder)):
#                 dist_from_start[i] = min(remainder[i]-start, n-(remainder[i]-start))
#             for i, val in enumerate(dist_from_start):
#                 if val > d:
#                     include.append(remainder[i])
#             result[len(include)].append(include) 
#             # d 반경 안에 있지 않은 것들만 리스트에 담는다. 

#         return remainder
    
#     cnt = 0
#     for i in range(len(dist)): # 인부마다 
#         remain_weak = rm_weak(dist[i], weak)
#         cnt += 1
#         if len(remain_weak) == 0:
#             return cnt
#         if i == len(dist)-1 and len(remain_weak) != 0:
#             return -1
#     return answer

def solution(n, weak, dist):
    dist.sort(reverse=True)
    vis = [True]*n
    for i in weak:
        vis[i] = False
        
    for d in dist:
        
    answer = 0

    return answer