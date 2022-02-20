def solution(id_list, report, k):
    from collections import defaultdict 
    answer = []
    temp = defaultdict(list)
    
    for elems in list(set(report)):
        a, b = elems.split()
        if a not in temp[b]:
            temp[b].append(a)
    
    print(temp)
    qty_dict = defaultdict(int)
    for key, val in temp.items():
        if len(val) >= k:
            for rep in val:
                qty_dict[rep] += 1
    for id in id_list:
        answer.append(qty_dict[id])

    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2))
# print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"], 3))