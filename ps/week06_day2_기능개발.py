'''
통과 코드 

내 코드 
'''
from collections import deque
import math

def solution(progresses, speeds):
    # 남은 일수를 계산해서 remain_day deque에 넣는다. 
    # 앞에서 하나씩 빼서 max_delay 값을 비교하고 
    # 더 크다면, append 시켜주고, max_delay값을 갱신
    # 더 작다면, 가장 마지막 원소에 cnt += 1
    answer = []
    remain_day = deque([])
    for i in range(len(progresses)):
        remain_day.append(math.ceil( (100-progresses[i]) /speeds[i]) )
    
    max_delay = 0
    while remain_day:
        temp = remain_day.popleft()
        if max_delay < temp:
            max_delay = temp
            answer.append(1)
        else: # lower than max_delay
            answer[-1] += 1
    return answer


'''
통과 코드

다른 사람 풀이과정 활용 (zip/ 음수를 이용한 올림 활용)
def solution(progresses, speeds):
    # zip을 활용하면 더 간단
    # 올림을 안하려면 음수로 만들어서 나누고 다시 -를 붙이면 된다. 
    answer = []
    for progress, speed in zip(progresses, speeds):
        remain_day = -((progress - 100)//speed)

        if not answer or answer[-1][0] < remain_day:
            answer.append( [remain_day, 1] )
        else:
            answer[-1][1] += 1

    return [i[1] for i in answer]
'''

        
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

