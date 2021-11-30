# 첫째 줄에 0~9,+, -
# 연속해서 두개이상 연산자는 없고 5자리보다 많이 연속되는 숫자는 없다. 
# 식의 길이는 50보다는 작거나 같다. 

import sys

a = input()

minus_split = a.split('-')
plus_split = []
for string in minus_split:
    plus_split.append(sum(map(int, string.split('+'))))
    
ans = 0
if len(plus_split) > 1:
    for i in range(1, len(plus_split)):
        plus_split[0] -= plus_split[i]
ans = plus_split[0]
print(ans)