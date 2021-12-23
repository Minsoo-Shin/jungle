# 정수 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을때 이 수가 적혀있는 숫자카드를 상근이가 몇개가지고 있는지

'''import bisect 

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
reqs = list(map(int, input().split()))

for req in reqs:
    print(bisect.bisect_right(card, req)- bisect.bisect_left(card, req), end=" ")'''


# n = int(input())
# card = list(map(int, input().split()))
# card.sort()

# m = int(input())
# reqs = list(map(int, input().split()))

def misect_left(l, req):
    idx = 0
    left, right = 0, len(l)
    while left <= right:
        mid = (left+right)//2
        print("*****",l[mid])
        if l[mid] < req:
            print("++++",mid)
            left = mid + 1
        else: # mid >= req:
            idx = mid
            print("----",mid)
            right = mid - 1
        print("\n")
    return idx

print(misect_left([1,2,2,2,3,4,5], 3))




