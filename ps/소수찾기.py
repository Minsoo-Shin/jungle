# # 소수가 몇 개인지 확인 (소수를 구하는 함수)
# # numbers의 숫
# import math 
# from itertools import permutations

# def _find(nums):
#     ans_cnt = []
#     # 모든 숫자마다 
#     for num in nums: #10, 11, 110
#         if num == 0 or num == 1 : continue
#         # 1, 제곱근까지의 숫자를 나눠 cnt를 더한다.
#         cnt = 0
#         for i in range(1, int(math.sqrt(num))+1):
#             if num % i == 0:
#                 cnt += 1
#                 if cnt > 1: break # cnt 3 부터 소수가 아니다.
#         if cnt == 1:
#             ans_cnt.append(num) 
#     return len(ans_cnt)
        
# def solution(numbers):
#     test_list = []
#     for i in range(1, len(numbers)+1):
#         test_list.extend([int("".join(one)) for one in set((permutations(list(numbers), i)))])
#     test_list = set(test_list)
#     answer = _find(test_list)
#     return answer

# print(solution("17"))



import math
from itertools import permutations

def find_(numbers):
    answer = 0
    for num in numbers:
        if num == 0 or num == 1: continue
        print(num)
        cnt = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                cnt += 1
        if cnt == 1:
            answer += 1   
    return answer

def solution(numbers):
    temp_list = list(numbers)
    temp = []
    for i in range(1, len(temp_list)+ 1):
        temp.extend([int("".join(j)) for j in set(permutations(temp_list, i))]) 
    temp = set(temp) # 0이라는 숫자로 인해 동일한 값이 들어올 수 있다. 11, 011 => 11
    return find_(temp)


print(solution("011"))