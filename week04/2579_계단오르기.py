'''
# 계단오르기

- 문제 설명
 > 계단을 오르면서 각 계단의 점수를 얻는 최대값을 구하라
 > 계단은 한 계단 or 두 계단
 > 연속된 세 개의 계단은 모두 밟을 수 없다. 

- 입력값
 > 계단 수 : n (<=300)
 > 계단 마다의 점수 : sco (<= 10,000)

- 문제 접근
 > 계단마다 쪼개서 최대값을 구하는 DP문제
 > 한 계단 전 or 두 계단 전에서 최종
 > 제약 조건은 연속된 세 개의 계단은 밟을 수 없네

점화식은 
일반
D[n] = max(D[n-1], D[n-2]) + sco[n]
D[n] = max(D[n-3] + sco[n-1] + sco[n], D[n-2] + sco[n])
'''
import sys
input = sys.stdin.readline

n = int(input())
sco = [0]
for i in range(n):
    sco.append(int(input()))

D = [0] * (n+1)
if n == 1:
    D[1] = sco[1]
elif n >= 2:
    D[1], D[2] = sco[1], sco[1] + sco[2]

for i in range(3, n+1):
    D[i] = max(D[i-3] + sco[i-1] + sco[i], D[i-2] + sco[i])

print(D[n])
