from collections import Counter
def solution(N, stages):
    answer = []
    fail = Counter(stages) # stages의 값은 1, 2, 3으로 시작
    passCnt = [0]*(N+1) # passCnt의 경우에는 index 0이 stage 1을 의미
    
    for s in stages:
        for i in range(0, s):
            passCnt[i] += 1
    
    temp = []
    for i in range(len(passCnt)):
        if passCnt[i] != 0:
            temp.append([ i+1, fail[i+1]/passCnt[i] ])
        else:
            temp.append([i+1, 0])
            
    print(temp)
    temp = temp[:-1]
    temp.sort(key = lambda x: x[1], reverse = True)
    for i in temp:
        answer.append(i[0])
    
    return answer