from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []
    # 판매 이익금은 dict(int)타입으로 각각 모든 구성원들을 돌면서 업데이트해주면 되겠네? 
    # graph 만들기 방향은 단방향 위로 향하게
    # amount * 100
    # if 0.1 * 100 * amount로 계산하여 내림하고 
    
    graph = defaultdict(list)
    profitTable = defaultdict(int)
    
    for i, j in zip(enroll, referral):
        if j == '-': continue
        graph[i].append(j)
    
    for start, amount in zip(seller, amount):
        stack = [[start, amount * 100]]
        while stack:
            print(stack)
            node, profit = stack.pop()
            if int(profit * 0.1) != 0: 
                profitTable[node] += profit - int(profit * 0.1)
                for next in graph[node]:        
                        stack.append([next, int(profit * 0.1)])
            else:
                profitTable[node] += profit
    
    for i in enroll:
        answer.append(profitTable[i])

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],	["young", "john", "tod", "emily", "mary"],	[12, 4, 2, 5, 10]))