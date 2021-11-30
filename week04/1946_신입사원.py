# 테스트 케이스 1<= T <= 20
# 지원자 숫자 1<= N <= 100,000
# 서류심사 성적, 면접 성적의 순위
# 동석차가 없다. 
# 서류 심사 결과와 면접 성적이 다른 지원자보다 모두 떨어지면 합격시키지 않는다. 

# 구하는 값은 선발할 수 있는 최대 인원 수

import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    newcomer = [list(map(int, input().split())) for _ in range(n)]
    newcomer.sort(key = lambda x: x[0])
    #[ [3,2], [1,4], [4,1], [2,3], [5,5] ]

    low_grade = newcomer[0][1]
    cnt = 1
    for i in range(1, n):
        if newcomer[i][1] < low_grade:  
            # 이미 확인한 지원자들은 서류심사 순위가 다 높은 상태이다. 나머지 면접 순위도 낮으면 뽑을 이유가 없다. 
            cnt +=1 
            low_grade = newcomer[i][1]
    
    print(cnt)
