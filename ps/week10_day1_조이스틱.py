# 맨 처음 A로만 이루어져있음
# 이미 맨처음에 AAA가 만들어져있음
# 커서는 처음의 위치에서 시작하고, 시작을 맞추고
# min(차례로 역순으로)
# 현재의 커서 위치가 필요한다. curr
# 다음의 커서 위치를 지정한다. next
# bfs로 A가 아닌 지점으로 가서 A로 변경하고 이동한다. 
from collections import deque

alpha = ['A', 'B', 'C', 'D' ,'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def solution(name):
    answer = 0
    for each in name:
        answer += alpha.index(each)
    print(answer)
    q = deque([[0, name, 0]])
    while q:
        temp = q.popleft()
        for dx in [1, -1]:
            s_idx, string, cnt = temp[0], temp[1], temp[2]
            # while string[s_idx] == 'A':
            #     s_idx += dx
            #     cnt += 1
            # 모든 문자열이 'A'라면 answer += cnt넣고 종료
            if len(string) == string.count('A'):
                answer += cnt
                return answer
            n_idx = s_idx + dx
            if string[n_idx] == 'A': cnt += 1
            else:
            # A가 아닌 부분이 나온다면 A로 변경하고 q에 넣어준다. 
                string = string[:n_idx] + 'A' + string[n_idx+1:]
            q.append([n_idx, string, cnt])

print(solution("JAN"))



    # 0 1 2 3 4 5 6 7 8 9 10
    # 0 x 0 x x x x x 0 0 0