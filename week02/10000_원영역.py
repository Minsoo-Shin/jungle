n=int(input()) # 원의 갯수를 입력
a=[]           # 입력받기 위한 리스트 선언
for i in range(n): 
	x,r=map(int,input().split())  # 원의 중심, 반지름을 입력받고
	a.extend([(0, x-r), (1, x+r)]) # x절편 두개를 Tuple형식으로 저장해준다. 0은 왼쪽/1은 오른쪽을 의미

a = sorted(a, key= lambda x: (x[1], -x[0]))
 # sort를 X절편 오름차순 기준/ R(1),L(0) 순으로
stack = []
area_qty = 1
# x절편으로 원을 이해해보자. 
for i in range(2*n): 
    if a[i][0] == 0: # 원의 왼쪽편이면, Stack에 일단 저장
        stack.append(a[i])
    else:           # 원의 오른쪽편이라면, 바로 이전의 나왔던 왼쪽과 원을 이룬다고 보면 된다. 
        compare = 0
        while True:
            left_side = stack.pop()      #(바로 이 전의 원이 아니라면 원과 원이 교차하기에 문제에 어긋난다.)
            if left_side[0] == 0:
                stack.append((2, a[i][1]-left_side[1])) #2를 원으로 간주, 그리고 원의 지름과 함께 저장
                area_qty += 1
                
                if compare > 0 and (a[i][1] - left_side[1]) == compare:
                    area_qty += 1
                break

            else: # left_side[0] == 2 
                compare += left_side[1]
            
print(area_qty)