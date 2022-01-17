# 사람 옮기기. 한번에 최대 두명씩, 무게 제한도 있음
# 몇 개의 구명 보트가 필요한지
'''
한사람씩 뽑고 같이 탈 수 있는 가장 무거운 사람을 골라서 리스트에서 뺸다.
그런 사람이 없다면 remove한다. 

# '''
# from collections import deque

# def solution(people, limit):
#     people.sort()
#     people = deque(people)
#     boat = 0
#     # 딱 적당한 숫자 limit - 한사람 무게
#     while people:
#         light = people.popleft()
#         boat += 1
#         save = []
#         for i in range(len(people)):
#             if light + people[i] <= limit:
#                 save.append(people[i])
#         if save:
#             people.remove(save[-1])
            
#     return boat

# print(solution([70, 50, 80, 50], 100))

##############################################
# from collections import deque
# import bisect 

# def solution(people, limit):
#     people.sort()
#     people = deque(people)
#     boat = 0
#     # 딱 적당한 숫자 limit - 한사람 무게
#     while people:
#         light = people.popleft()
#         idx = bisect.bisect(people, limit-light)
#         if idx != 0:
#             people.remove(people[idx-1])
#         boat += 1    
#     return boat

# 정확성  테스트
# 테스트 1 〉	통과 (42.79ms, 10.3MB)
# 테스트 2 〉	통과 (1.54ms, 10.3MB)
# 테스트 3 〉	통과 (21.64ms, 10.3MB)
# 테스트 4 〉	통과 (25.39ms, 10.3MB)
# 테스트 5 〉	통과 (9.40ms, 10.4MB)
# 테스트 6 〉	통과 (1.28ms, 10.3MB)
# 테스트 7 〉	통과 (3.37ms, 10.3MB)
# 테스트 8 〉	통과 (0.06ms, 10.2MB)
# 테스트 9 〉	통과 (0.24ms, 10.2MB)
# 테스트 10 〉	통과 (15.15ms, 10.3MB)
# 테스트 11 〉	통과 (18.17ms, 10.3MB)
# 테스트 12 〉	통과 (12.77ms, 10.3MB)
# 테스트 13 〉	통과 (10.64ms, 10.2MB)
# 테스트 14 〉	통과 (1.77ms, 10.3MB)
# 테스트 15 〉	통과 (0.13ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
##############################################


# import bisect 
# def solution(people, limit):
#     people.sort()
#     boat = 0
#     deleted = [False] * len(people)
#     # 딱 적당한 숫자 limit - 한사람 무게
#     left, right = 0, len(people)
#     for i in range(len(people)):
#         if deleted[i] == True: continue
#         light = people[i]
#         deleted[i] == True
#         while left <= right:
#             mid = (left + right)//2
#             # 합쳐서 제한선이 될 수 있는 무게 : limit - light
#         if idx != 0:
#             deleted[idx-1] == True
        
#         boat += 1    
#     return boat

# print(solution([70, 50, 80, 50], 100))

# def solution(people, limit):
#     people.sort()
#     boat = 0
#     deleted = [False] * len(people)
#     # 딱 적당한 숫자 limit - 한사람 무게
#     for j in range(len(people)):
#         if deleted[j] != True:
#             deleted[0] = True
#             light = people[j]
#             boat += 1
#             save = []
#             for i in range(j+1, len(people)):
#                 if deleted[i] != True and people[i] <= limit-light:
#                     save.append(i)
#             if save:
#                 deleted[save[-1]] = True                
#     return boat

# print(solution([70, 50, 80, 50], 100))

# 정확성  테스트
# 테스트 1 〉	통과 (683.72ms, 10.4MB)
# 테스트 2 〉	통과 (426.43ms, 10.3MB)
# 테스트 3 〉	통과 (334.65ms, 10.3MB)
# 테스트 4 〉	통과 (309.28ms, 10.3MB)
# 테스트 5 〉	통과 (104.39ms, 10.2MB)
# 테스트 6 〉	통과 (35.21ms, 10.3MB)
# 테스트 7 〉	통과 (76.81ms, 10.3MB)
# 테스트 8 〉	통과 (1.18ms, 10.2MB)
# 테스트 9 〉	통과 (2.72ms, 10.3MB)
# 테스트 10 〉	통과 (268.08ms, 10.3MB)
# 테스트 11 〉	통과 (227.66ms, 10.4MB)
# 테스트 12 〉	통과 (221.34ms, 10.3MB)
# 테스트 13 〉	통과 (301.62ms, 10.3MB)
# 테스트 14 〉	통과 (589.08ms, 10.3MB)
# 테스트 15 〉	통과 (5.42ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)



# 투 포인터
def solution(people, limit):
    people.sort()
    boat = 0   
    left, right = 0, len(people)-1
    while left <= right:
        if people[left] + people[right] > limit:
            right -= 1
            boat += 1 
        else:
            left += 1
            right -= 1
            boat += 1
    return boat

print(solution([70, 50, 80, 50, 100], 150))