import sys

n = int(input())
stack = []

for i in range(n):
    line = sys.stdin.readline().split()

    if line[0] == 'push':
        stack.append(int(line[1]))

    if line[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(int(stack.pop()))

    if line[0] == 'size':
        print(len(stack))

    if line[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    if line[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(int(stack[-1]))