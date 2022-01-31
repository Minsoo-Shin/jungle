# a = 1
# cnt = 1
# for i in range(2, a + 1):
# 	if a % i == 0: cnt += 1
# if cnt == 2:
# 	print("소수입니다.")
# else:
#     print("소수가 아닙니다.")

import math 
a = 1
cnt = 1
if a == 0 or a == 1:
    print("소수아님")
else:
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0: cnt += 1
    if cnt == 1:
        print("소수")
    else:
        print("소수아님")