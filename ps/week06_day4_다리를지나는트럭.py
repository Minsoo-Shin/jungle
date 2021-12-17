# bridge_length : 2 => deque length 
# weight : 총 무게
# truck_weights : 트럭들의 무게 => []
'''
while True:
    cur = 다리에 접근하는 트럭의 무게
    if 두 번째 조건은 트럭 무게와 다리 위치무게[1:] 합친값이 <= weight이면
        cur = popleft()
    else:
        cut = 0

    다리위치별 무게.popleft()
    다리위치별 무게.append(cur)
    time += 1

    if sum(다리위치별 무게) == 0:
        break
ruturn time




[0] * 10000
weight제한 10000
truck_weight = 10000

    
'''
# 
# time = 0 : 시간이 지날때마다 cnt
# list

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_list = deque([0]*bridge_length) # [0, 0]
    truck_weights = deque(truck_weights) # [20, 20, 20]
    cur = 0 #다리에 접근하는 트럭의 무게

    weight_sum = sum(bridge_list)
    while True:
        temp = bridge_list.popleft()
        weight_sum -= temp
        if truck_weights and (truck_weights[0] + weight_sum <= weight):
            cur = truck_weights.popleft()
        else:
            cur = 0
        
        bridge_list.append(cur)
        weight_sum += cur
        time+=1
    
        if weight_sum == 0:
            break
    return time

print(solution(2, 10, [7,4,5,6]))
    