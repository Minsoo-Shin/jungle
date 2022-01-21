# 단품 메뉴 조합: 최소 2가지 이상 단품메뉴로 구성
# 2명이상 주문된 단품메뉴 조합에 대해서만 후보군으로 선정

# 알고리즘 
# for i in coure별로 2, 3, 4
# 2의 경우, 


# 알고리즘 (orders)
# 모든 오더들을 하나하나 비교한다. 
# 'XYZ', 'XWY', 'WXA'
# 'XYZ' 기준에선 'XY', 'X'
# 'XWY' 기준에서 'WX'
# defaultdict(int) 갯수를 올려준다. 
    # key를 만들떈 ''.join(sorted(list))
# candidates = [#,#,{}, ] {'XY':2, 'WX':2}
#         0 1 2 3

# for문을 돌면서 max값이 되면 max_list를 비워주고 
# max_list가 만들어 졌으면 answer에 extend하면 된다. 
from collections import defaultdict
from itertools import combinations, permutations

def solution(orders, course):
    answer = []
    courses = [defaultdict(int) for _ in range(course[-1]+1)] # coures[-1] : 찾아야하는 코스 요리 수의 최대값

    # 두 문자열을 비교해가면서 공통 가능한 조합들을 구한다. 
    candidates = []
    for i in range(len(orders)):
        for j in range(i+1, len(orders)):
            w1, w2 = orders[i], orders[j]
            str_list = []
            for word in w1:
                if word in w2:
                    str_list.append(word)
            for k in range(2, len(str_list)+1):
                for perm in combinations(str_list, k):
                    candidates.append(''.join(sorted(perm)))
    candidates = list(set(candidates))
    # candidates = ['ACDE', 'BCFG', 'CDE', 'AC']

    #'AC': cnt, 'CDE' : cnt, 'ACDE': cnt, 'BCFG' : cnt

    # candidates = ['ACDE', 'BCFG', 'CDE', 'AC']
    for candidate in candidates:
        len_candi = len(candidate)
        # 원하는 course의 수가 아닐 경우 pass
        if len_candi not in course: continue
        
        # orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
        # candidate가 orders에 포함되어있는 수를 계산해서 courses에 저장한다. 
        for i in range(len(orders)):
            cnt = 0
            for one_elem in candidate:     # candidate = 'ACDE', one_elem = 'A'
                if one_elem in orders[i]:
                    cnt += 1
            if cnt == len_candi:
                courses[len_candi][candidate] += 1
    
    # course를 돌면서 원하는 코스 요리의 수마다 가장 많이 선택한 조합을 answer에 저장
    #     dict의 value기준으로 정렬해서 가장 큰 값을 고른다. 
    for c in course:
        temp_dict = courses[c]
        max_course = []
        max_cnt = 0
        for key, value in temp_dict.items():
            if max_cnt < value:
                max_cnt = value
                max_course.append(key)
            elif max_cnt == value:
                max_course.append(key)
        answer.extend(max_course)

    return sorted(answer)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["ABCD", "ABCD", "ABCD"], [2,3,4]))

