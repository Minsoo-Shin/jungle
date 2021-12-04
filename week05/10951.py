# while True:
#     try:
#         a, b = map(int, input().split())
#     except:
#         break
#     print(a+b)

# import sys
# for line in sys.stdin:
#     print(sum(map(int, line.split())))

import sys
for line in sys.stdin:
    print(line.split())
    print(type(line.split()))

