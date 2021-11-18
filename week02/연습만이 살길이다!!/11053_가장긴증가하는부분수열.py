# 맨 뒤에 있는 원소를 선택해서 이전에 만들어놓은 원소의 수열 갯수를 이용한다. 
import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
count = [1] * n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            count[i] = max(count[i], count[j] + 1)

print(max(count))
    

