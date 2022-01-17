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
    length = len(name)

    for each in name:
        position = alpha.index(each)
        answer += min(position, 26 - position)

    #bfs를 돌린다. 
    q = deque([[0, name, 0]])
    while q:
        temp = q.popleft()
        for dx in [1, -1]:
            s_idx, string, cnt = temp[0], temp[1], temp[2]
            # 땜빵은 힘들다 1 (idx가 마이너스가 되면 아래 if문의 string 변경해주는 부분이 에러가 난다.)
            
            if s_idx < 0: s_idx += length
            # A가 아닌 부분이 나온다면 A로 변경한다. 
            if string[s_idx] != 'A':
                string = string[:s_idx] + 'A' + string[s_idx+1:]

            # 다 변경되었는지를 확인한다. 
            if length == string.count('A'):
                answer += cnt
                return answer
            # 다 변경 안되었을때 인덱스를 이동하면서 CNT를 늘려준다. 
            else:
                n_idx = s_idx + dx
                cnt += 1
                # 땜빵은 힘들다 2 (name의 길이 이상을 안 갖도록 미리미리 챙기자)         
                if  n_idx >= length: n_idx -= length
                elif n_idx <= -(length+1): n_idx -= length   
                q.append([n_idx, string, cnt])

print(solution("ABABAABA"	))



    # 0 1 2 3 4 5 6 7 8 9 10
    # 0 x 0 x x x x x 0 0 0