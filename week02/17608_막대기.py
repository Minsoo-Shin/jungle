import sys

# 높은 막대기만 stack에 저장하고, 
# 오른쪽의 막대기가 더 크다고 하면 이전에 stack과 비교해서 낮거나 같으면 pop

n = int(input())
stack = []

for _ in range(n):
    height = int(sys.stdin.readline())
    # len(stack)가 0이면 원소 추가
    if len(stack) == 0:
        stack.append(height)
    else: 
        while len(stack) != 0: # 이전전 원소도 재확인 하기 위해
            if height >= stack[-1]:
                stack.pop()
            else:
                break
        stack.append(height)
print(len(stack))



