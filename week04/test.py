'''
동전 문제 

입력값)
- 테스트 케이스 : t (10개)
- 동전의 갯수 : n (20개 이하)
- 동전의 종류 : unit (10000원 이내)
- 금액 : m (10,000원 이하())

문제 분석)
- 동전 unit 돌면서 최소 공배수이면, 따로 처리?
  : 리스트에 있는 동전의 최소 공배수를 구하는 방법? 한번에 떠오르질 않네
    => 동전의 경우의 수를 구하는거라 위의 방법과는 관련없음. 
    (단지 최소 동전의 갯수를 이용할때만 사용)
    ####################################################
    시간 복잡도
    : lcs 재귀함수로 log(N)미만? 따라서 종합적으로는 NlogN이 되지 않을까 생각된다.  

    def lcs(a,b):
    if a % b == 0: return b
    else: return lcs(b, a%b)

    result = 1
    for i in units:
        result = (result * i)/lcs(result, i)
    if m % result == 0:
        tmp = 0
        # 오름차순으로 정렬되어있다는 문제의 가정에 한함
        for i in range(len(units)-1, -1, -1):
            tmp += m // units[i]
            m %= units[i]
            if m == 0:
                break
        print(tmp)
    ####################################################
- 동전 경우의 수는 작은 단위의 경우의 수를 이용해나갈 수 있다. 
'''
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):  
    n = int(input())
    units = list(map(int, input().split()))
    m = int(input())

    D = [0] * (m+1)
    D[0] = 1
    
    for unit in units:
        for i in range(unit, m+1):
            D[i] += D[i-unit]

    print(D[m])

