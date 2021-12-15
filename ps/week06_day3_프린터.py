# # 통과 

# # 내 코드
# # 우선순위가 높은 작업이 있다면 현재의 작업은 맨 뒤로 미룬다.
# from collections import deque

# def solution(priorities, location):
#     order = 0 # 프린트되면 +=1
#     # 한바퀴돌면 location을 알기 어렵기 떄문에 미리 기록해준다. 
#     print_order = deque([(idx, val) for idx, val in enumerate(priorities)])
#     while print_order:
#         loc, priority = print_order.popleft()
#         if len(print_order) == 0:
#             order += 1 
#             break
#         # 나머지 작업들과 우선순위 비교
#         for i in range(len(print_order)):
#             if priority < print_order[i][1]: 
#                 print_order.append((loc, priority))
#                 break
#             if i == len(print_order)-1:
#                 order += 1
#                 if loc == location: 
#                     return order
#     return order
    
# print(solution([1], 0))
#############################################################################
# 통과 

# 다른 사람 코드 참고
# Tuple 형태나 list형태도 첫번쨰 원소로 max, min이 가능하다. 
# print_order가 계속 pop되는 형태이니 리스트가 있는지 없는지 확인해줘야함
from collections import deque

def solution(priorities, location):
    order = 0 # 프린트되면 +=1
    # 한 바퀴 돌면 location을 알기 어렵기 떄문에 미리 기록해준다. 
    print_order = deque([(val, idx) for idx, val in enumerate(priorities)])
    while print_order:
        priority, loc = print_order.popleft()

        if print_order and max(print_order)[0] > priority:
            print_order.append((priority, loc))
        else:
            order += 1
            if loc == location: break
    return order
    
print(solution([1, 1, 9, 1, 1, 1], 0))

# max 함수 기능 확인
# a = [(1, 3), (2, 4), (1, 5)]
# print(max(a)[1])
#############################################################################
# 통과

# # 다른 사람 코드
# # any(iterable) : iterable의 객체에 하나라도 True가 존재하면 True를 반환
# # all(iterable) : iterable의 객체 모두가 True이라면 True를 반환

# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer