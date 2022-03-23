'''
1. 아이디어
    일반적으로 서칭하면 n2
    이분탐색으로
    for문 돌면서 
        search(num) 존재하면 1을 반환
2. 시간 복잡도
    NlogN
3. 자료구조
    str, end, mid = int
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split()))

def search(st, en, tar):
    mid = (st + en)//2
    if st == en:
        if arr[mid] == tar:
            print(1)
        else:
            print(0)
        return
        
    if arr[mid] >= tar:
        search(st, mid, tar)
    else:
        search(mid+1, en, tar)

for num in arr2:
    st = 0
    en = n-1
    search(st, en, num)