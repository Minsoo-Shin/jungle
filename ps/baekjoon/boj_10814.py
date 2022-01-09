# import sys
# input = sys.stdin.readline

# n = int(input())
# mem = []
# for i in  range(n):
#     temp = input().split()
#     int(temp[0])
#     print(type(temp[0]))
#     mem.append(temp)

# mem.sort()
# for i in range(n):
#     print(*mem[i])


import sys
input = sys.stdin.readline

n = int(input())
user = [input().split() for _ in range(n)]

user.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(user[i][0], user[i][1])