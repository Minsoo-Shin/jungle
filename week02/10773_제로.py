import sys

n = int(input())
stack = []
for i in range(n):
    # 라인마다 입력을 받아서
    line = int(sys.stdin.readline())
    # 들어온값이 0이 아니면 stack에 저장하고
    if line != 0:
        stack.append(line)
    # 들어온값이 0이면 가장 최근값 stack[-1]값을 방출한다. 
    else:
        stack.pop()
# 다 돌고 나서 이제껏 stack에 쌓인 수를 총합을 한다. 

print(sum(stack))