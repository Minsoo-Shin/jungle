from decimal import Decimal
def solution(lines):
    answer = 0
    # 초 기준으로 변환 (float)
    # (처리 시작, 처리 완료 시점)
    # 완료 시점을 기준으로 정렬한다. 
    # 하나씩 완료시점을 순회하면서 1초 범위에 들어와있는 막대그래프가 있는지 확인한다. 
    reqList = []
    for line in lines:
        line = line.split(" ")
        reqStart, spend = line[1], line[2]
        h, m, s = map(float, reqStart.split(':'))
        reqSec = h * 3600 + m * 60 + s
        reqList.append([float(Decimal(str(reqSec)) - Decimal(spend[:-1]) + Decimal('0.001')), reqSec])
        
    reqList.sort(key = lambda x : x[1])
    for i in range(len(reqList)):
        check = 1
        for j in range(i+1, len(reqList)):
            if reqList[j][0] < reqList[i][1] + 1:
                check += 1
        answer = max(answer, check)
              
    return answer