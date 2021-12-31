# graph 문제
# 가능한 모든 경로를 찾는다. 
# n = set으로 방문해야하는 모든 나라의 수를 구한다. 
# 티켓으로 탐색한 cnt가 == n과 동일하면 ans리스트에 append한다. 
# 두 개 이상이면 알파벳 순 sort()하고 첫번째 원소 출력
    # 아닐 경우 그냥 출력
    # 없는 경우는 없다. 

# from collections import defaultdict
# def solution(tickets):
#     def dfs(start):
#         stack = [[1, start]] # [ [방문 나라 수, "ICN"] ]
#         while stack:
#             schedule = stack.pop()
#             depart = schedule[-1]
#             for next in graph[depart]: # next = "JFK" 등
#                 if next not in schedule:
#                     schedule.append(next)
#                     schedule[0] += 1
#                     if schedule[0] == n:
#                         answer.append(schedule[1:])
#                     else:
#                         stack.append(schedule)
                    
                    
#         # 방문할수 없는 경우는 없다. 
    
#     answer = []
#     nations = set()
#     graph = defaultdict(list)
#     for temp in tickets:
#         graph[temp[0]].append(temp[1])

#     for temp in tickets:
#         nations.add(temp[0])
#         nations.add(temp[1])
#     n = len(set(nations))
#     # 출발지 마다 dfs를 한다 
#     for ticket in tickets:
#         dfs('ICN')
    
#     answer.sort()
#     return answer[0]

# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))



# from collections import defaultdict
# def solution(tickets):
#     def dfs(start):
#         stack = [[start]] # [ ["ICN"] ]
#         while stack:
#             schedule = stack.pop()
#             depart = schedule[-1]
#             for next in graph[depart]: # next = "JFK" 등
#                 schedule.append(next)

#                 if len(set(schedule)) == n:
#                     answer.append(schedule)
#                     return
#                 else:
#                     stack.append(schedule)
                    
                    
#         # 방문할수 없는 경우는 없다. 
    
#     answer = []
#     nations = set()
#     graph = defaultdict(list)
#     for temp in tickets:
#         graph[temp[0]].append(temp[1])

#     for temp in tickets:
#         nations.add(temp[0])
#         nations.add(temp[1])
#     n = len(set(nations))

#     dfs("ICN")
    
#     answer.sort()
#     print(answer)
#     return answer[0]

# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))


'''
처음 시작을 ICN으로 넣고, DFS로 돈다.  
갈 수 있는 여행지를

# 1. 티켓을 다 써야한다. 
# 2. 첫 출발은 ICN공항이다. 
# 3. 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
'''
from collections import defaultdict
def solution(tickets):
    def dfs(start):
        stack = [ [0, start] ]
        spend = [False] * len(tickets)

        while stack:
            schedule = stack.pop()
            for i in range(len(tickets)):
                cnt, depart = schedule[0], schedule[-1]
                if depart == tickets[i][0]:
                    if spend[i] == False:
                        spend[i] = True
                        if cnt == len(tickets) - 1:
                            schedule.append(depart)
                            schedule[0] += 1
                            answer.append(schedule)
                        else:    
                            schedule[0] += 1
                            schedule.append(depart)
                            stack.append(schedule)
                

                    
    graph = defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    
    answer = []
    dfs("ICN")
    answer.sort()
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))


