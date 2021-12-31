# begin에 있는 단어를 target에 있는 단어로 변환.
# words리스트의 단어 중에 한글자만 다른 경우, next_visit큐에 넣는다. 
from collections import deque
def solution(begin, target, words):
    def match(a, b):
        cnt1 = 0
        for i in range(len(a)):
            if a[i] == b[i]: cnt1 += 1
        return cnt1 == len(a)-1

    answer = 0
    visited = [False] * len(words)
    que = [ [begin, 0] ]
    while que:
        tmp = que.pop(0)
        node, cnt = tmp[0], tmp[1]
        # 현재값과 한글자만 다른 단어를 words리스트에서 찾아 다음 후보리스트에 넣는다.
        for i in range(len(words)):
            # 정답이 아닐 경우, 다음 후보지를 물색한다. 
            if match(node, words[i]):
                if visited[i] == False:
                    visited[i] = True
                    if words[i] == target:
                        answer = cnt + 1
                        break
                    que.append( [words[i], cnt + 1] )
            
    return answer

print(solution("hit","cog",	["hot", "dot", "dog", "lot", "log", "cog"]))


# from collections import dequegit
# def solution(begin, target, words):
#     def match(a, b):
#         cnt1 = 0
#         for i in range(len(a)):
#             if a[i] == b[i]: cnt1 += 1
#         return cnt1 == len(a)-1

#     answer = 0
#     visited = [False] * len(words)
#     que = [ [begin, 0] ]
#     while que:
#         tmp = que.pop(0)
#         node, cnt = tmp[0], tmp[1]
#         # 현재값과 한글자만 다른 단어를 words리스트에서 찾아 다음 후보리스트에 넣는다.
#         for i in range(len(words)):
#             # 정답 return
#             if words[i] == target:
#                 answer = cnt + 1
#                 break
#             # 정답이 아닐 경우, 다음 후보지를 물색한다. 
#             if match(node, words[i]):
#                 if visited[i] == False:
#                     visited[i] = True
#                     que.append( [words[i], cnt + 1] )
            
#     return answer