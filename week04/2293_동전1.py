import sys
input = sys.stdin.readline
unit_ea, value = map(int, input().split()) 
unit_list = [int(input()) for _ in range(unit_ea)] # 1,2,5원 단위
d = [0] * (value + 1) #경우의 수 0을 기준으로 잡는다. 
d[0] = 1

for i in unit_list:
    for j in range(i, value+1):
        if j-i >=0: # 돈의 단위가 실제 구하는 값보다 낮으면 경우의 수를 셀 필요가 없음.
            d[j] += d[j-i] 
print(d[value])
