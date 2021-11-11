import sys

n = int(input())
array = [int(input()) for i in range(n)]

array.sort(reverse=True)
for num in array : print(num)