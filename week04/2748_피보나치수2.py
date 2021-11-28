import sys
'''
if n = 0:
    return 0
if n = 1:
    return 1

a(n) = a(n-1) + a(n-2)
a(5) = a(4) + a(3)
a(4) = a(3) + a(2) = 2 + 
a(3) = a(2)[= 1] + a(1)[= 1] = 2
a(2) = a(1) + a(0) = 1 + 0 = 1
'''

'''
시간 초과 
def pi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return pi(n-1) + pi(n-2)

n = int(sys.stdin.readline())
print(pi(n))

'''
n = int(sys.stdin.readline())
pi_value = [0] * 92
pi_value[0], pi_value[1] = 0, 1
for i in range(2, n + 1):
    pi_value[i] = pi_value[i-2] + pi_value[i-1]

print(pi_value[n])
