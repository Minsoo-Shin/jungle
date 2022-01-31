# from collections import defaultdict


# def solution(fees, records):
#     answer = []
#     base, base_f, unit, unit_f = fees
#     m_record = []
#     for record in records:
#         t, car, in_out = record.split()
#         h, m = map(int, t.split(":"))
#         m = h * 60 + m
#         m_record.append([car, m])
#     # [5961, 200분]

#     fee = defaultdict(list)
#     for record in m_record:
#         if record[0] not in fee:
#             fee[record[0]].append(record)
#         else:
#             spend = record[1] - fee[record[0]][0][1] 
#             answer.append([record[0], spend])
#             fee.pop(record[0])
#     for key, val in fee.items():
#         if len(val) != 0:
#             spend = (23*60+59)-val[0][1]
#             answer.append([key, spend])

#     answer.sort()
#     ans = []
#     for i in answer:
#         if ans and ans[-1][0] == i[0]:
#             ans[-1][1] += i[1]
#         else:
#             ans.append(i)
#     for i in range(len(ans)):
#         if ans[i][1] <= base:  
#             ans[i].append(base_f)
#         else:
#             ans[i].append( base_f + ( -((base-ans[i][1])//unit) ) * unit_f )

#     return [i[2] for i in ans]

from collections import defaultdict
import math 

def solution(fees, records):
    answer = []
    base, base_f, unit, unit_f = fees
    fee = defaultdict(int)
    for record in records:
        t, car, in_out = record.split()
        h, m = map(int, t.split(":"))
        m = h * 60 + m
        if in_out == 'IN':
            fee[car] += (23*60 + 59) - m
        else:
            fee[car] -= (23*60 + 59) - m
    for key, val in fee.items():
        if val <= base:
            answer.append([key, base_f])
        else:
            answer.append([key, base_f + math.ceil((val-base)/unit) * unit_f])
    answer.sort()
    return [i[1] for i in answer]


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

print(solution([120, 0, 60, 591],	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))

print(solution([1, 461, 1, 10],	["00:00 1234 IN"]))