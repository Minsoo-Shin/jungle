# 문자열 Valid Parenthesis String, VPS)인지를 판단하는 함수이다. 

# '(' 문자가 들어오면 stack에 일단 저장하고, ')'라는 문자열이 들오면
# stack에 가장 마지막 원소를 pop한다. 
# len(stack) == 0: print(yes)

import sys
n = int(input())

for _ in range(n):
    line = sys.stdin.readline()
    # 언제 초기화할지 항상 염두해둬야 오류가 없음
    stack = []
    for string in line:
        if string == "(":
            stack.append(string)
        elif string == ")":
            if len(stack) == 0:
                stack.append(string)
                break
            else:
                stack.pop()
    
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
