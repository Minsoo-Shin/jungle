# 통과 

# 내 풀이 (정렬쓸땐 bisect로 푸는게 좋구나)

# I 숫자: 큐를 삽입/ D1 큐에서 최댓값 삭제/D-1 최솟값 삭제
# 
# 입력 명령어는 10^6, nlogn으로 풀어야하고, 입력숫자는 음수가 될 수도 있다. 
# [최대값, 최소값] 을 반환한다. 
# 빈큐에 대한 예외 처리 - 빈 큐에 삭제하라는 연산이라면 무시

# 큐 하나는 최소값 또는 최대값만 알 수 있다.
# 큐 [원소, -원소]

import bisect

def solution(operations):
    num = []
    for op in operations:
        op = op.split()
        
        # Insert 명령
        if op[0] == "I":
            # 아무것도 없으면 그냥 넣고
            if len(num) == 0: num.append(int(op[1]))
            else: bisect.insort(num, int(op[1]))
        # Delete 명령
        else:
            if len(num) == 0: continue
            # 최소값 제거
            if op[1] == "-1":
                num.pop(0)
            # 최대값 제거
            else:
                num.pop()
    # 결과 반환
    if len(num) == 0: 
        return [0,0]
    else: 
        return [num[-1], num[0]]
            
print(solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"] ))



