import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

# 열 처음부터 for문을 돌리는데 큰 height가 나오면 값을 인덱스와 함께
# 같이 업데이트한다. 그러고 바로 arr[i]를 확인하고 stack을 확인해서 바로 출력한다. 
stack = []

for i in range(n):
    if len(stack) == 0:
        stack.append((arr[i],i))
        print(0, end=' ')
    else:
        j = -1
        while True: # stack[j] 지수를 다 확인했다면, 0을 출력해야한다. 
            if arr[i] < stack[j][0]: # 오른쪽에 stack이 더 크다고 하면,,,
                print(stack[j][1] + 1, end=' ')
                break
            elif abs(j) == len(stack):
                print(0, end=' ')
                break
            else:
                j -= 1
        stack.append((arr[i],i))