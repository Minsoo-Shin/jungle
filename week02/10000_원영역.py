n=int(input())
a=[]
for i in range(n):
	x,r=map(int,input().split())
	a.append((x-r,x+r))
stack = []
circle = []
sorted(a, key = lambda x : (-x[0], x[1]))

for i in range(n):
    if a[i][0] == 'L':
        stack.append(a[i])
    else:
        j=-1
        while stack[j][0] == 'L':
            temp = stack.pop()
            stack.append(('C', a[i][1] - stack[j][1])) # 원의 지름을 계산해서 stack 리스트에 append
        if stack[j][0] == 'C':
            ssum = 0
            while True:    
                temp1 = stack.pop()
                ssum += temp1[1]
                
