# [점수 이외, 점수]형식으로 만든다. 
# 점수 기준으로 정렬한다. 
# bisect로 왼쪽 idx, 오른쪽 idx 확인한다. 
# 그리고, [왼쪽 idx: 오른쪽 idx + 1]내에서 for문 돌면서 확인하면서 answer += 1

# 점수 이외에는 하나로 합쳐서 한번에 확인
import bisect 

def solution(info, query):
    answer = []
    many = len(info)
    info_m = [[0] for _ in range(many)]
    left_idx, right_idx = 0, 0
    score = []
    
    for i in range(many):
        temp = info[i].split(' ')
        info_m[i][0] = int(temp.pop())
        score.append(info_m[i][0])
        temp = ' '.join(temp)
        info_m[i].append(temp)
    print(info_m)

    query_m = [[0] for _ in range(len(query))]
    for i in range(len(query)):
        temp1 = query[i].split(" and ")
        query_m = temp1[-1].split(" ")[1] # 숫자
        query_m.extend()

        

    score.sort()
    info_m.sort(key = lambda x: x[0])
    bisect.bisect(score, )


    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))